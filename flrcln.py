o
    8B�bI
  �                   @   s�  d dl Z e �d� d dl Z e �d� e �d� ed� d dlZd dl Z d dlZd dlZd dlZdZdZdZ	d	Z
d
ZdZdZdZdd� Zd dlZd dlZd dlZd dlZd dlZd dlZd dlmZ eed � d dlZd dlZd dlZd dlmZ d dlmZmZmZmZ d dlZd dlmZ d dlZd dlZd dlZd dlmZ eeed e
 ��Ze�d� dZed Ze� Zded< ded< eed< ejeed�Z ejeed�Z e �� d dkr�eed  e	 e �� d! d"  d � e �� d! d# Z!e�d� g Z"ee	d$ e d% e
 d �Z#d&Z$eje$ed�Z%e#�rbe!D ]Z&eed' e	 d( e e&d)  � e"�'e&d) � �qz!e"D ]Z(ed* e( Ze�d� ejeed�Z eee j) � �q6W n   ed+� e�d� Y eee	d, e
 d- e	 d. ��Z*e �d� e�d� dS )/�    N�clearzlolcat banner.pyzpython x.py�
z[1;90mz[1;91mz[1;92mz[1;93mz[1;94mz[1;95mz[1;96mz[1;97mc                 C   s2   | d D ]}t j�|� t j��  t�d� qd S )Nr   g{�G�z�?)�sys�stdout�write�flush�time�sleep)ZpudinaZword� r
   �	flrcln.py�	logoprint   s
   
�r   )�CaseInsensitiveDictz 
)r	   )�init�Fore�Back�Stylez[>] Enter Api Key: �   z5https://circle.robi.com.bd/mylife/appapi/appcall.php?zop=getFollowerInfoList�gzipz
User-AgentZ(000oc0so48owkw4s0wwo4c00g00804w80gwkw8kgz	x-app-keyz	x-api-key)�headersZrdescZOKz[>] Total Follower:�data�totalZfollowerz

	[!]z+ If You Wonna To Clear Follower List Type Yz�https://circle.robi.com.bd/mylife/appapi/appcall.php?op=performAction&app_version=81&action=kast&msgId=62&msisdn=8801875409158&message=Your Circle  Follower List Is Cleaning By Using Mr. TooLS....!! &retry=falsez[>]z CIRCLE ID	:	 �nicknamezop=blockUser&nickname=zError!z	 

	Pressz Enterz To Exit)+�os�system�printZasyncior   Zrequestsr   ZbiblackZbiredZbigreenZbiyellowZbiblueZbipurpleZbicyanZbiehiter   ZjsonZrequests.structuresr   Zcoloramar	   r   r   r   r   �str�input�x�baseZurlr   ZpostZresp�yZfolNicks�boolZurlxZresp5�user�appendr   �textZxnr
   r
   r
   r   �<module>   s�   



$
 
�
 
