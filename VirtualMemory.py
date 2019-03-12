import psutil
import os,datetime


pc_mem = psutil.virtual_memory()

div_gb_factor = (1024.0 ** 3)

print('\n\n')

print('您的CPU逻辑核心数为%s\t个\n' % (psutil.cpu_count()))

print('CPU的物理核心数为%s\t个\n' % (psutil.cpu_count(logical=False)))

print("内存总量: %f\tGB\n" % float(pc_mem.total / div_gb_factor))

print("可用内存总量: %f\tGB\n" % float(pc_mem.available / div_gb_factor))

print("已用内存量: %f\tGB\n" % float(pc_mem.used / div_gb_factor))

print("内存使用百分比: %f" % float(pc_mem.percent), '%\n')

print("可用内存:%f\tGB\n" % float(pc_mem.free / div_gb_factor))

print('系统开机时间%s\n' % datetime.datetime.fromtimestamp(psutil.boot_time()).strftime("%Y-%m-%d %H:%M:%S"))

print("按回车键退出程序！")

input()


