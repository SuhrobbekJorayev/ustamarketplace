import os
from imagekitio import ImageKit


imagekit = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY")
)


def upload_avatar(file):
    response = imagekit.files.upload(
        file=file.read(),
        file_name=file.name,
        folder="/avatars"
    )

    return response.url