/*
設定可以上傳的檔案副檔名
呼叫執行 axuploader.js, 將檔案以批量直接存至伺服器硬碟
嘗試同時將檔案透過 Google Drive API 存至對應的雲端硬碟
用於將各上傳檔案名稱存入資料庫中, 檔案刪除時從資料庫中移除
*/
function sendToServer(files){
    var req = new XMLHttpRequest();
    var result = document.getElementById('result');
    req.onreadystatechange = function()
    {
      if(this.readyState == 4 && this.status == 200) {
        result.innerHTML = this.responseText;
      } else {
        result.innerHTML = "working...";
      }
    }
    
    // 利用 POST 將上傳檔案名稱數列送至 server, 準備存入資料庫
    req.open('POST', '/saveToDB', true);
    req.setRequestHeader('content-type', 'application/x-www-form-urlencoded;charset=UTF-8');
    req.send("files=" +  files);
}

$(document).ready(function(){
$('.prova').axuploader({url:'fileaxupload', allowExt:
['jpg','png','gif','7z','pdf','zip','flv','stl','swf'],
finish:function(x,files)
    {
        // 這裡要利用 sendToServer 函式將 files 數列傳到 server, 再由 python 納入資料庫
        sendToServer(files);
        alert('All files have been uploaded: '+files);

    },
enable:true,
remotePath:function(){
return 'downloads/';
}
});
});