import os
import sys
import dropbox
from io import StringIO
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


dbx = dropbox.Dropbox(os.environ['DROPBOX_API_KEY'])


def upload_to_dropbox(file, uploadpath):
    print("Uploading file to Dropbox as " + uploadpath + "...")
    try:
        dbx.files_upload(file.read(), uploadpath, mode=WriteMode('overwrite'))
    except ApiError as err:
        if err.error.is_path() and \
                err.error.get_path().reason.is_insufficient_space():
            sys.exit("ERROR: Cannot back up; insufficient space.")
        elif err.user_message_text:
            print(err.user_message_text)
        else:
            print(err)


def download_from_dropbox(remotepath, localpath):
    print("Downloading " + remotepath + " from Dropbox to" + localpath + "...")
    try:
        md, res = dbx.files_download(remotepath)
        with open(localpath, "wb") as fout:
            fout.write(res.content)
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    except IOError as err:
        print('*** IOError', err)
        return None
    return localpath


def delete_from_dropbox(remotepath):
    print("Delete " + remotepath + " from Dropbox")
    try:
        md = dbx.files_delete(remotepath)
    except dropbox.files.DeleteError as err:
        print('*** Api error', err)
