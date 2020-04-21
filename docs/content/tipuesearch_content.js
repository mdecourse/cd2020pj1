var tipuesearch = {"pages": [{'title': 'About', 'text': 'Course:  https://mde.tw/cd2020 \n KMOLab, Department of Mechanical Design Engineering, National Formosa University, Taiwan. \n This project is mainly used with  https://mde.tw/cd2020  repository to demonstrate how to apply Python and Dart programs to build web-based tools to enhance the effectiveness of the mechanical collaborative product design. \n Website:  https://mde.tw/cd2020pj1 \n Repository:  https://github.com/mdecourse/cd2020pj1 \n', 'tags': '', 'url': 'About.html'}, {'title': 'Streaming', 'text': '問卷: \n 請登入 ＠gm 帳號後, 填寫下列問卷. \n 第八與第九週上課是否繼續採用線上方式進行 \n 結果: \n \n 第十週之後的分組方式 \n \n 2a w7 Youtube + OBS live streaming video: \n \n \n 2b Meet + Youtube +OBS \n \n \n', 'tags': '', 'url': 'Streaming.html'}, {'title': 'Windows', 'text': 'Use Firefox to conduct  https://meet.google.com  online meeting. Since we are using G Suite for Education, meeting recording and live stream functions are available. \n Use Firefox to connect to  https://youtube.com  and add live stream video with OBS streaming integrated withYoutube server.', 'tags': '', 'url': 'Windows.html'}, {'title': 'Mac', 'text': 'Use Safari to conduct  https://meet.google.com  online meeting. Since we are using G Suite for Education, meeting recording and live stream functions are available. \n Even with System Preferences to grant "Screen Recording" privacy setup, Firefox does not allow user to share screen operation during online Google Handout Meet session. \n Use Firefox to connect to  https://youtube.com  and add live stream video with OBS streaming integrated withYoutube server.', 'tags': '', 'url': 'Mac.html'}, {'title': 'CMS', 'text': 'Use Google + Domain API to setup login for @gm.nfu.edu.tw users \n https://console.developers.google.com \n Setup  OAuth 2.0 Client IDs  \n Use  https://github.com/authomatic/authomatic  to allow user login with Google or Github accounts.', 'tags': '', 'url': 'CMS.html'}, {'title': 'Python', 'text': '', 'tags': '', 'url': 'Python.html'}, {'title': 'Dart', 'text': 'Use dart2js to compile Dart html program into javascript and interacted with Flask program. \n   Clear Canvas   Draw ROC   Draw USA \n', 'tags': '', 'url': 'Dart.html'}, {'title': 'Flask', 'text': 'Python and Flask \n Login to your gm email account and download  2019_ABeginnersGuideToPython3Programming.pdf \n Login to your gm email account and download  2019_BuildingRESTAPIsWithFlask.pdf \n The most important feature of REST is its statelessness, which simply means that neither the client nor the server has to know the state of each other to be able to communicate. In this way, both the client and the server can understand any message received without seeing the previous message. \n', 'tags': '', 'url': 'Flask.html'}, {'title': 'Database', 'text': '', 'tags': '', 'url': 'Database.html'}, {'title': 'Linkages', 'text': '\n \n', 'tags': '', 'url': 'Linkages.html'}, {'title': 'Solvespace', 'text': 'https://github.com/solvespace/solvespace \n', 'tags': '', 'url': 'Solvespace.html'}, {'title': 'Pyslvs-UI', 'text': 'https://github.com/KmolYuan/Pyslvs-UI \n', 'tags': '', 'url': 'Pyslvs-UI.html'}, {'title': 'Range3', 'text': 'https://github.com/Range-Software/range3 \n', 'tags': '', 'url': 'Range3.html'}, {'title': 'Mechatronics', 'text': '', 'tags': '', 'url': 'Mechatronics.html'}, {'title': 'Arduino', 'text': 'https://www.makerspaces.com/wp-content/uploads/2017/02/Arduino-For-Beginners-REV2.pdf \n', 'tags': '', 'url': 'Arduino.html'}, {'title': 'Picsimlab', 'text': 'https://github.com/lcgamboa/picsimlab \n Download  picsimlab_0_7_5_win64_setup.exe  (only for @gm users) \n', 'tags': '', 'url': 'Picsimlab.html'}, {'title': 'Unoardusim', 'text': 'https://www.sites.google.com/site/unoardusim/ \n Download  UnoArduSimV2.7.1.zip  (only for @gm users) \n', 'tags': '', 'url': 'Unoardusim.html'}, {'title': 'CoppeliaSim', 'text': 'https://www.coppeliarobotics.com/ \n Download\xa0 CoppeliaSim_Edu_V4_0_0_Win.zip  (for @gm users only) \n', 'tags': '', 'url': 'CoppeliaSim.html'}, {'title': 'RemoteAPI', 'text': 'Download\xa0 web_vrep2.zip  (for @gm users only) \n Download\xa0 CoppeliaSim_4_Self_Driving_Car_Simulation.7z  (for @gm users only) \n When execute python remote api, opencv-python and imutils modules are needed. \n pip install opencv-python \n pip install imutils \n DefaultCamera with threaded child script and start the simRemoteApi on port 19999. \n simRemoteApi.start(19999) \n Therefore user can control the simulated model through the CoppeliaSim_Server_IP on port 19999. \n clientID = vrep.simxStart(\'CoppeliaSim_Server_IP\',19999,True,True,5000,5) # Get the client ID \n Use \n While True: \n to replace \n for i in range(150): \n the image of the remote vision sensor will be sent to the remote API client through  https://pypi.org/project/opencv-python/ \n reading and display vision sensor image using python remoate api ( 來源 ) \n 改為 Python 3 相容 \n # -*- coding: utf-8 -*-\n"""\nCreated on Sun Jul 05 15:01:58 2015\n\n@author: ACSECKIN\n\npython -m pip install opencv-python\n"""\n\nimport vrep\nimport time\nimport cv2\nimport numpy as np\n\nvrep.simxFinish(-1)\n\nclientID = vrep.simxStart(\'127.0.0.1\', 19997, True, True, 5000, 5)\n\nif clientID!=-1:\n    print(\'Connected to remote API server\')\n    print(\'Vision Sensor object handling\')\n    res, v1 = vrep.simxGetObjectHandle(clientID, \'vs1\', vrep.simx_opmode_oneshot_wait)\n    print(\'Getting first image\')\n    err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v1, 0, vrep.simx_opmode_streaming)\n    while (vrep.simxGetConnectionId(clientID) != -1):\n        err, resolution, image = vrep.simxGetVisionSensorImage(clientID, v1, 0, vrep.simx_opmode_buffer)\n        if err == vrep.simx_return_ok:\n            print("image OK!!!")\n            img = np.array(image,dtype=np.uint8)\n            img.resize([resolution[1],resolution[0],3])\n            cv2.imshow(\'image\',img)\n            if cv2.waitKey(1) & 0xFF == ord(\'q\'):\n                break\n        elif err == vrep.simx_return_novalue_flag:\n            print("no image yet")\n            pass\n        else:\n          print(err)\nelse:\n  print("Failed to connect to remote API Server")\n  vrep.simxFinish(clientID)\n\ncv2.destroyAllWindows() \n pythonBubbleRob.pdf \n lua_one_link_remote_api.7z \n V-rep 系統目錄中的\xa0remoteApiConnections.txt 可以同時啟動多個 port 允許多 client 連線: \n // This file defines all the continuous remote API server services (started at remote API plugin initialization, i.e. V-REP start-up)\n//\n// Each remote API server service requires following 3 entries:\n//\n// portIndex@_port = xxxx               // where xxxx is the desired port number (below 19997 are preferred for server services starting at V-REP start-up)\n// portIndex@_debug = xxxx              // where xxxx is true or false\n// portIndex@_syncSimTrigger = xxxx     // where xxxx is true or false. When true, then the service will be pre-enabled for synchronous operation.\n//\n// In above strings, @ can be any number starting with 1. If more than one server service is required, then numbers need to be consecutive and starting with 1\n\n// Let\'s start a continuous remote API server service on port 19997:\nportIndex1_port             = 19997\nportIndex1_debug            = false\nportIndex1_syncSimTrigger   = true\n\nportIndex2_port             = 19998\nportIndex2_debug            = false\nportIndex2_syncSimTrigger   = true\n \n 在遠端的多台電腦, 可以利用 \n clientID = vrep.simxStart(\'Server_IP\', 19997, True, True, 5000, 5) \n 與 \n clientID = vrep.simxStart(\'Server_IP\', 19998, True, True, 5000, 5) \n 同時對 rempte API server 進行操控, 各 client 並可以透過上述程式取得 rempte API Server 運作時的影像, 以便利用各 client 中的 python 程式對遠端 V-rep 模擬進行遠端操控. \n 例如: 兩名使用者分別在不同電腦上對同一台 rempte API Server 中的不同四輪車模型進行操控. \n 以下為另外一個參考程式: \n import vrep\n\nprint(\'Program started\')\nvrep.simxFinish(-1) # just in case, close all opened connections\nclientID=vrep.simxStart(\'127.0.0.1\',19999,True,True,5000,5)\nif clientID!=-1:\n    print(\'Connected to remote API server\')\n    res,v0=vrep.simxGetObjectHandle(clientID,\'Vision_sensor\',vrep.simx_opmode_oneshot_wait)\n    res,v1=vrep.simxGetObjectHandle(clientID,\'PassiveVision_sensor\',vrep.simx_opmode_oneshot_wait)\n\n    res,resolution,image=vrep.simxGetVisionSensorImage(clientID,v0,0,vrep.simx_opmode_streaming)\n    while (vrep.simxGetConnectionId(clientID)!=-1):\n        res,resolution,image=vrep.simxGetVisionSensorImage(clientID,v0,0,vrep.simx_opmode_buffer)\n        if res==vrep.simx_return_ok:\n            res=vrep.simxSetVisionSensorImage(clientID,v1,image,0,vrep.simx_opmode_oneshot)\n    vrep.simxFinish(clientID)\nelse:\n    print(\'Failed connecting to remote API server\')\nprint(\'Program ended\') \n 此外 system 目錄下的\xa0usrset.txt 可以進行客製化設定 \n 參考資料 \n Virtual Experiments Design for Robotics Based on V-REP.pdf \n Pyrep: bringing V-rep to deep robot learning.pdf \n Controlling your robot with Python.pdf', 'tags': '', 'url': 'RemoteAPI.html'}, {'title': 'Webots', 'text': 'https://cyberbotics.com/ \n \n \n', 'tags': '', 'url': 'Webots.html'}]};