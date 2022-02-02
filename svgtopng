#! /bin/bash
names=( * )
shopt -s extglob
shopt -s dotglob
shopt -s globstar
declare -a FILELIST
for f in ${names[@]};
do 
    #FILELIST[length_of_FILELIST + 1]=filename
    FILELIST[${#FILELIST[@]}+1]=$(echo "$f");
done
for i in ${FILELIST[@]}
do
   echo "${i}"
   fuckyoubash=`echo ${i} | sed 's/....$//'`
   myvar=`echo ${i} | sed 's/svg$//'`
   myvar="${myvar}png"
   echo $myvar
   rsvg-convert "${fuckyoubash}".svg -o $myvar
done
