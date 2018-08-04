#!/bin/bash
PROJ_NAME="TP_webinfo"
if [ `tmux ls|grep "no server running"` ];then
    echo hello
elif [[ `tmux ls|grep $PROJ_NAME` ]];then
    mux start TP_webinfo
else
    tmux a -t $PROJ_NAME
fi
    
