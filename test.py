import wmi


def get_windows_system_info():
    info_str = ""
    try:
        c = wmi.WMI()

        # 获取操作系统基本信息
        os_info = c.Win32_OperatingSystem()[0]
        info_str += f"操作系统名称: {os_info.Name}\n"
        info_str += f"操作系统版本: {os_info.Version}\n"
        info_str += f"操作系统制造商: {os_info.Manufacturer}\n"
        info_str += f"操作系统安装日期: {os_info.InstallDate}\n"

        # 获取计算机系统信息
        computer_system = c.Win32_ComputerSystem()[0]
        info_str += f"计算机名称: {computer_system.Name}\n"
        info_str += f"计算机制造商: {computer_system.Manufacturer}\n"
        info_str += f"计算机型号: {computer_system.Model}\n"

        # 获取CPU信息
        for cpu in c.Win32_Processor():
            info_str += f"CPU名称: {cpu.Name}\n"
            info_str += f"CPU核心数: {cpu.NumberOfCores}\n"
            info_str += f"CPU线程数: {cpu.ThreadCount}\n"

        # 获取内存信息
        total_memory = 0
        for memory in c.Win32_PhysicalMemory():
            total_memory += int(memory.Capacity)
        info_str += f"总内存容量: {total_memory / 1024 / 1024 / 1024}GB\n"

        # 获取磁盘信息
        disk_info = ""
        for disk in c.Win32_DiskDrive():
            disk_info += f"磁盘型号: {disk.Model}\n"
            disk_info += f"磁盘容量: {int(disk.Size) / 1024 / 1024 / 1024}GB\n"
        info_str += f"磁盘信息:\n{disk_info}"

    except Exception as e:
        info_str += f"获取系统信息时出现错误: {e}"

    return info_str

print(get_windows_system_info())