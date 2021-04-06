import argparse
import os
from functions.Path import Path
from functions.tcp_syn_flood import syn_flood
from functions.ClockFunc import ClockFunc  # Demo
from functions.encryption import cryto
from functions.Ipconfig import Showip
from functions.shut import shut # benson871229
from functions.letter_frequency import frequency # benson871229
from functions.nmap import nmap  # benson871229
from functions.mkdir import notepad  # benson871229
from functions.Openyt import Openyt  # 豔婕
from functions.Bypassuac import Bypassuac  # 豔婕
from functions.Changepassword import Changepassword  # 豔婕
from functions.Netstat import Netstat  # 綺娟
from functions.Tracert import Traceip  # 綺娟
from functions.Nslookup import Nslookup
from functions.PortScanner import Scanport

def main():
    # 準備參數解析
    app_description = "校園資安測試常用工具集合"
    epilog_text = "歡迎至https://github.com/TwMoonBear-Arsenal/BetterCalculator/issues提供建議"
    parser = argparse.ArgumentParser(
        description=app_description, epilog=epilog_text)
    args = parser.parse_args()

    # 準備選單
    optionList = []
    optionList.append(ClockFunc())
    optionList.append(Netstat())
    optionList.append(Traceip())
    optionList.append(Bypassuac())
    optionList.append(Changepassword())
    optionList.append(Openyt())
    optionList.append(shut())
    optionList.append(frequency())
    optionList.append(nmap())
    optionList.append(notepad())
    print()

    # 以下持續循環直到使用者結束
    while(True):

        # 顯示選單
        os.system('cls')
        print(app_description)
        print(epilog_text)
        print("--------")
        for i in range(len(optionList)):
            print('[ {:>2} ]'.format(i+1), optionList[i].Description)
        print("[", 99, "]", "結束程式")

        # 詢問使用者
        selection = int(input("請輸入需要的功能：").strip())
        print()

        # 依使用者選號找出功能項
        if((selection - 1) < len(optionList)):
            func = optionList[selection-1]
            func.Run()
        elif(selection == 99):
            print("See you next time...")
            print()
            return
        else:
            print("輸入錯誤")

        # 開始下一循環
        print()
        input("按任意鍵繼續...")

if __name__ == "__main__":
    main()
