o
    ��b{  �                   @   s�  d dl Z e �d� d dlZd dl Z d dlZd dlZd dlZd dlZd dlZd dlZd dl Z d dlZd dlmZ dZdZ	dZ
dZdZd	Zd
ZdZd dlZd dlZd dlZd dl Z d dlZd dlmZ e �d� dd� Zeed � e�d�Zeed � ee
d � eed e
 d e d � e�d� eede�� d � eed � eed � 	 e �d� d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ e �d� ed e d ZeD ]Zej�e� ej��  e�d� q�d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ e
d ZeD ]Zej�e� ej��  e�d� �qeee	d  e ��Z e d!k�rEe �d"� e �d� d#Z �ne d$k�rXe �d%� e �d� d#Z �ne d&k�rje �d'� e �d� d#Z n�e d(k�r|e �d)� e �d� d#Z n�e d*k�r�e �d+� e �d� d#Z n�e d,k�r�e �d-� e �d� d#Z n�e d.k�r�e �d/� e �d� d#Z n�e d0k�r�e �d1� e �d� d#Z n�e d2k�r�e �d3� e �d� d#Z n�e d4k�r�e �d5� e �d� d#Z nte d6k�r�e �d7� e �d� d#Z nbe d8k�re �d9� e �d� d#Z nPe d:k�re �d;� e �d� d#Z n>e d<k�r0e �d=� e �d� d#Z n,e d>k�rBe �d?� e �d� d#Z ne d@k�rRe �dA� e �d� n
e dBk�r\e �dC� q�)D�    N�clear)�sleepz[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mzlolcat banner.pyc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )N�
�{�G�z�?)�sys�stdout�write�flush�timer   )ZpudinaZword� r   �mojib.py�	logoprint#   s
   
�r   z4
==================================================
zhttps://ipinfo.io/jsonz	 DEVELOPED BY : Mr. MoJiiBz	 VERSION 	  : 3.0u   	 ♥♥z	 Mr. MoJiiBr   z	 Your IP Addreds:- Zipz3
==================================================z$  To Stop Attack press CTRL + Z....
Tzpython ab.py)�init�Fore�Back�Styleu   [√]z Show Your Option
ak  
[01]	    API GENERATE
[02] 	    API TO NUMBER
[03] 	    ID TO NUMBER
[04] 	    NUMBER TO ID
[05] 	    CIRCLE PIN
[06]	    GET BLOCK LIST
[07] 	    AUTO SHOUT
[08]	    JOIN XJOIN
[09]	    AUTO POKE 
[10]  	    AUTO COM
[11]	    FOLLOWING CLEAN
[12]	    FOLLOWER CLEAN
[13]	    FOLLOWER
[14]	    FOLLOWING
[15]	    SHOUT CHECK
[16]	    CONNECT ADMIN
[17]	    EXIT
z
[>] Select Your Option: �1zpython api.pyr   �2zpython apitonb.py�3zpython idtonb.py�4zpython nbtoid.py�5zpython cpin.py�6zpython bl.py�7zpython st.py�8zpython jx.py�9zpython cp.pyZ10zpython com.pyZ11zpython flgcln.pyZ12zpython flrcln.pyZ13zpython flr.pyZ14zpython flg.pyZ15zpython allst.pyZ16z+xdg-open https://www.facebook.com/Mr.PudinaZ17�exit)!�os�systemZasyncior   Zrequestsr
   Zcoloramar   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   �getZresponse�printZjsonr   r   r   r   Zwords�charr   r   r	   �str�input�ar   r   r   r   �<module>   s�    




	




















































�