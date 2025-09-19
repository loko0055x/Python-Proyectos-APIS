import docker

client = docker.from_env()
keyword = "evolution-api"  # palabra clave para filtrar


def remove_containers(substring):
    containers = client.containers.list(all=True)
    for container in containers:
        name = container.name
        if substring in name:
            print(f" Deteniendo contenedor: {name}")
            if container.status == 'running':
                container.stop()
            print(f"  Eliminando contenedor: {name}")
            container.remove()
            print(f" Contenedor {name} eliminado.")


def remove_images(substring):
    images = client.images.list()
    for image in images:
        tags = image.tags
        if any(substring in tag for tag in tags):
            print(f"  Eliminando imagen: {tags}")
            try:
                client.images.remove(image.id, force=True)
                print(f"  Imagen {tags} eliminada.")
            except Exception as e:
                print(f"Error al eliminar imagen {tags}: {e}")


def remove_volumes(substring):
    volumes = client.volumes.list()
    for volume in volumes:
        if substring in volume.name:
            print(f" Eliminando volumen: {volume.name}")
            try:
                volume.remove(force=True)
                print(f"  Volumen {volume.name} eliminado.")
            except Exception as e:
                print(f"Error al eliminar volumen {volume.name}: {e}")


def remove_networks(substring):
    networks = client.networks.list()
    for network in networks:
        if substring in network.name:
            print(f"Eliminando red: {network.name}")
            try:
                network.remove()
                print(f"  Red {network.name} eliminada.")
            except Exception as e:
                print(f" Error al eliminar red {network.name}: {e}")


def remove_containers_by_name_or_volume(substring):
    containers = client.containers.list(all=True)
    for container in containers:
        name = container.name
        mounts = container.attrs.get('Mounts', [])
        uses_related_volume = any(substring in m.get(
            'Name', '') or substring in m.get('Source', '') for m in mounts)

        if substring in name or uses_related_volume:
            print(f"Eliminando contenedor: {name} ({container.id[:12]})...")
            if container.status == 'running':
                container.stop()
            container.remove()
            print(f"Contenedor {name} eliminado.")


def remove_images_by_name(substring):
    images = client.images.list()
    for image in images:
        tags = image.tags
        if any(substring in tag for tag in tags):
            print(f"Eliminando imagen: {tags}...")
            try:
                client.images.remove(image.id, force=True)
                print(f"Imagen {tags} eliminada.")
            except Exception as e:
                print(f"Error al eliminar imagen {tags}: {e}")


def remove_images_by_names(image_names):
    for image_name in image_names:
        try:
            image = client.images.get(image_name)
            print(f"Eliminando imagen {image_name}...")
            client.images.remove(image.id, force=True)
        except docker.errors.ImageNotFound:
            print(f"Imagen {image_name} no encontrada.")
        except docker.errors.APIError as e:
            print(f"Error al eliminar imagen {image_name}: {e}")


def remove_volumes_by_name(substring):
    volumes = client.volumes.list()
    for volume in volumes:
        if substring in volume.name:
            print(f"Eliminando volumen: {volume.name}...")
            try:
                volume.remove(force=True)
                print(f"Volumen {volume.name} eliminado.")
            except Exception as e:
                print(f"Error al eliminar volumen {volume.name}: {e}")


def remove_networks_by_name(substring):
    networks = client.networks.list()
    for network in networks:
        if substring in network.name:
            print(f"Eliminando red: {network.name}...")
            try:
                network.remove()
                print(f"Red {network.name} eliminada.")
            except Exception as e:
                print(f"Error al eliminar red {network.name}: {e}")


if __name__ == "__main__":
    print("\n Limpiando contenedores relacionados...")
    print("\n Limpiando redes relacionadas...")
    remove_networks_by_name(keyword)
    remove_containers_by_name_or_volume(keyword)

    print("\n Limpiando volúmenes relacionados...")
    remove_volumes_by_name(keyword)

    print("\n Limpiando imágenes relacionadas...")
    remove_images_by_name(keyword)
    remove_images_by_names(['redis:latest', 'postgres:15'])
    print(" Buscando y eliminando recursos relacionados con 'evolution'...\n")

    remove_containers(keyword)
    remove_volumes(keyword)
    remove_images(keyword)
    remove_networks(keyword)

    print("\n Limpieza completada. Todos los recursos de Evolution API han sido eliminados.")
    print(" Otros contenedores (como n8n) no fueron tocados.")
    print("\n Limpieza completada.")
