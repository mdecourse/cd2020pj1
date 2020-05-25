from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth()
gauth.LoadClientConfigFile("./../client_secrets.json")
#gauth.LocalWebserverAuth() # client_secrets.json need to be in the same directory as the script
drive = GoogleDrive(gauth)

'''
# View all folders and file in your Google Drive
fileList = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
for file in fileList:
  print('Title: %s, ID: %s' % (file['title'], file['id']))
  # Get the folder ID that you want
  # 檔案會上傳到根目錄下的 uploaded  目錄中
  if(file['title'] == "uploaded"):
      fileID = file['id']
'''
# GDrive 上 uploaded 目錄的 fileID
with open("./../uploaded_id.txt", 'r') as content_file:
    fileID = content_file.read()

#fileID = "your_folder_file_ID"

fileName = "ModernC.pdf"
filePath = "./test/"
file1 = drive.CreateFile({"mimeType": "application/pdf", "parents": [{"kind": "drive#fileLink", "id": fileID}], "title":  fileName})
file1.SetContentFile(filePath + fileName)
file1.Upload() # Upload the file.
#print('Created file %s with mimeType %s' % (file1['title'], file1['mimeType']))   
print("upload fileID:" + str(file1['id']))
file2 = drive.CreateFile({'id': file1['id']})
file2.GetContentFile('./test/downloaded_ModernC.pdf') # Download file as 'downloaded_ModernC.pdf under directory test'.

'''
file1.Trash()  # Move file to trash.
file1.UnTrash()  # Move file out of trash.
file1.Delete()  # Permanently delete the file.
'''
