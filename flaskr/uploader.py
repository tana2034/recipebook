from flaskr.dropbox_file import upload_to_dropbox, download_from_dropbox, delete_from_dropbox


class Uploader:
    def upload(self, file, uploadpath):
        raise NotImplementedError()

    def download(self, remotepath, localpath):
        raise NotImplementedError()

    def delete(self, remotepath):
        raise NotImplementedError()


class DropBoxUploader(Uploader):
    def upload(self, file, uploadpath):
        return upload_to_dropbox(file, uploadpath)

    def download(self, remotepath, localpath):
        return download_from_dropbox(remotepath, localpath)

    def delete(self, remotepath):
        return delete_from_dropbox(remotepath)
