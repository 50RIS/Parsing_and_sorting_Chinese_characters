#!/bin/bash

# 大家好！
# by Boris Zubov (鲍里斯) contact@technodrive.ru

# The characters for sorting by UTF-8 numbers come from the previous ch.py script by pype, like
# ./ch.py | ./sort_Chinese_characters.sh | less
column_from_py_ch=$(cat)

utf8_from_characters=$(echo -n)

for planet in $column_from_py_ch
do
	tmp=$(echo -n ${planet} | hexdump | head -1 | cut -f2,3 -d ' ' | sed -e "s/ 00//")
	tmp=$(echo '\x'${tmp:2:2}'\x'${tmp:0:2}'\x'${tmp:4:2})
	# echo $tmp ; echo -e "$tmp" ; exit
	
	utf8_from_characters=${utf8_from_characters}${tmp}$'\n'
done

utf8_from_characters=$(echo "${utf8_from_characters}" | grep '.' | uniq | sort -V)

# echo "${utf8_from_characters}" ; exit

# echo "$utf8_from_characters"

for planet in $utf8_from_characters
do
	echo -e "$planet"
done
