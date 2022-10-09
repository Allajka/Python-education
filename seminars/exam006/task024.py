# Написать программу вычисления арифметического выражения заданного строкой.
# Используются операции +,-,/,*. приоритет операций стандартный.
# Пример: 2+2 => 4; 1+2*3 => 7; 1-2*3 => -5;
# Добавить возможность использования скобок, меняющих приоритет операций. Пример: 1+2*3 => 7; (1+2)*3 => 9;

st = input()
for el in ['+', '-', '*', '/']:
    st = st.replace(el, f' {el} ')
st_list = st.split()

for i in range(len(st_list)-1):
    if st_list[i] == '*':
        result = int(st_list[i-1]) * int(st_list[i+1])
        st_list[i] = result
        st_list[i-1] = None
        st_list[i+1] = None
st_list = [el for el in st_list if el != None]

