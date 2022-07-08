import socket
import datetime
import Rooky2
import asyncio
import time

print('Введите сторону (left|right): ')
side = input()
print('Введите COM порт (example: COM2): ')
print('Примечание: Обычно COM2 для правой руки, COM7 - для левой.): ')
print('Если выдаёт ошибки, в диспетчере устройств проверить COM порты.): ')

COMport = input()
print('Введите port для сервера (правая 9091; левая 9090): ')
print('Если в мобильном приложении менялись порты, то стороны рук поменяюся ')
ServerPort = int(input())
print('Для работы с другой рукой, запустите приложение ещё раз, не закрывая это')

arm = Rooky2.Rooky(COMport, side)
def ShakeHands():

    arm.reset_joints()


    print('Touch sensor to start action')
    arm.move_joints([{
        'name': '{0}_arm_4_joint'.format(side),
        'degree': 70
    }, ], 1.5);
    arm.move_joints([{
        'name': '{0}_arm_1_joint'.format(side),
        'degree': 10
    }, ], 0.5);
    while True:
        # Ждем касания датчика
        if not arm.is_touched():
            continue
        for count in range(7):
            arm.move_joints([{
                'name': '{0}_arm_4_joint'.format(side),
                'degree': 50
            }, ], 0.3);
            arm.move_joints([{
                'name': '{0}_arm_4_joint'.format(side),
                'degree': 70
            }, ], 0.3);
        arm.move_joints([{
            'name': '{0}_arm_1_joint'.format(side),
            'degree': 0
        }, ], 0.5);
        arm.move_joints([{
            'name': '{0}_arm_4_joint'.format(side),
            'degree': 0
        }, ], 1.5);
        arm.reset_joints()
        # side ="left"
        # arm = Rooky2.Rooky('COM7', side)
        # arm.clear()
        # arm = Rooky2.Rooky(" ", " ")
        # arm = None

        break
def BegIt():
    arm.reset_joints()
    arm.calibration()
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 3);
    arm.move_joints([{
        "name": "{0}_arm_7_joint".format(side),
        "degree": 74
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 65
    }, {
        "name": "{0}_arm_1_joint".format(side),
        "degree": -25
    }, ], 3);
    for count in range(10):
        if arm.get_servo_angle(1) == -25:
            arm.move_joints([{
                "name": "{0}_arm_1_joint".format(side),
                "degree": 15
            }, ], 1);
            time.sleep(0.65)
        elif arm.get_servo_angle(1) == 15:
            arm.move_joints([{
                "name": "{0}_arm_1_joint".format(side),
                "degree": -25
            }, ], 1);
            time.sleep(0.65)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 3);
    arm.reset_joints()
def ComeAtMe():
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 3)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 34
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 74
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": -74
    }, ], 3);
    for count in range(4):
        arm.move_joints([{
            "name": "{0}_arm_7_joint".format(side),
            "degree": 74
        }, ], 1/2);
        arm.move_joints([{
            "name": "{0}_arm_7_joint".format(side),
            "degree": 0
        }, ], 1/2);
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 3);
def HighFive():
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 3);
    arm.reset_joints()
    arm.calibration()
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 134
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 70
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 47
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 70
    }, ], 5);
    time.sleep(2)
    while True:
        # Ждем касания датчика
            if not arm.is_touched():
                continue
            arm.move_joints([{
                "name": "{0}_arm_3_joint".format(side),
                "degree": -20
            }, ], 2);
            arm.move_joints([{
                "name": "{0}_arm_3_joint".format(side),
                "degree": 70
            }, ], 1);
            time.sleep(2)
            arm.move_joints([{
                "name": "{0}_arm_1_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_2_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_3_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_4_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_5_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_6_joint".format(side),
                "degree": 0
            }, {
                "name": "{0}_arm_7_joint".format(side),
                "degree": 0
            }, ], 3);
            break
def RoboDance():
    arm.move_joints([{
        "name": "{0}_arm_4_joint".format(side),
        "degree": 80
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_2_joint".format(side),
        "degree": 83
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 92
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_3_joint".format(side),
        "degree": 83
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, ], 1);
    for count in range(3):
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 60
        }, ], 1);
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 80
        }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 134
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 51
    }, ], 2);
    time.sleep(5)
    arm.move_joints([{
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, ], 1);
    time.sleep(2)
    arm.move_joints([{
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, ], 1);
    time.sleep(1)
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, ], 1);
def CoolerStance():

    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 60
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 20
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_3_joint".format(side),
        "degree": 20
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_4_joint".format(side),
        "degree": 60
    }, ], 2);
    time.sleep(5)
    if arm.is_touched():
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 0
        }, ], 2);
        arm.move_joints([{
            "name": "{0}_arm_3_joint".format(side),
            "degree": 0
        }, ], 2);
        arm.move_joints([{
            "name": "{0}_arm_1_joint".format(side),
            "degree": 0
        }, {
            "name": "{0}_arm_2_joint".format(side),
            "degree": 0
        }, ], 2);
    else:
        arm.move_joints([{
            "name": "{0}_arm_1_joint".format(side),
            "degree": 90
        }, {
            "name": "{0}_arm_2_joint".format(side),
            "degree": 0
        }, {
            "name": "{0}_arm_4_joint".format(side),
            "degree": 0
        }, ], 1);
        arm.move_joints([{
            "name": "{0}_arm_1_joint".format(side),
            "degree": 60
        }, {
            "name": "{0}_arm_2_joint".format(side),
            "degree": 20
        }, {
            "name": "{0}_arm_4_joint".format(side),
            "degree": 60
        }, ], 1);
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, ], 2);
    arm.move_joints([{
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, ], 2);
def EndlessWave():
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 5);
    arm.reset_joints()
    arm.calibration()
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 134
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 70
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 47
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 70
    }, ], 5);
    while True:
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 35
        }, ], 1);
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 70
        }, ], 1)
    arm.reset_joints()
    arm.calibration()
def Wave():
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 5);
    arm.reset_joints()
    arm.calibration()
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 134
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 70
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 47
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 70
    }, ], 5);
    for count in range(5):
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 35
        }, ], 1);
        arm.move_joints([{
            "name": "{0}_arm_4_joint".format(side),
            "degree": 70
        }, ], 1);
    arm.move_joints([{
        "name": "{0}_arm_1_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_2_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_3_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_4_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_5_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_6_joint".format(side),
        "degree": 0
    }, {
        "name": "{0}_arm_7_joint".format(side),
        "degree": 0
    }, ], 5);
    arm.reset_joints()
    arm.calibration()


conn = socket.socket()
conn.bind(('', ServerPort))
conn.listen(1)
print(socket.gethostbyname(socket.gethostname()))

while True:
    try:
        client, addr = conn.accept()
        print('connected:', addr)
    except socket.error:
        pass
    else:
        data = client.recv(1024)
        message = 'Запрос доставлен'
        bytes_encoded = message.encode('utf-16')
        current_date_time = datetime.datetime.now()
        current_time = current_date_time.time().replace(microsecond=0)
        print(current_time, ':', data.decode('utf-16', 'replace'))
        CLientMessage = data.decode('utf-16', 'replace')
        message2 = 'Робот поднял руку'
        MessageToClient = message2.encode('utf-16')

        if (CLientMessage == "Shake"):
            ShakeHands()
        # if (CLientMessage == "Stance"):
        #     await Stance()
        # if (CLientMessage == "Beg"):
        #     await BegIt()
        if (CLientMessage == "HighFive"):
             HighFive()
        # if (CLientMessage == "RoboDance"):
        #     await RoboDance()
        if (CLientMessage == "Stance"):
             CoolerStance()
        if (CLientMessage == "Hello"):
             Wave()
        if (CLientMessage == "Taunt"):
             ComeAtMe()
        if (CLientMessage == "EHello"):
             EndlessWave()

