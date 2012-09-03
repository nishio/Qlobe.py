v=0000;s="""import zlib,struct                  ,math,sys,re;d=re.sub('\s+|".*'
'"',"", '''^Lcf<LK8,_@7gj*       "%.#%  :::##"       LJ=c5nM)Tp1g0%Xv.,S[<>YoP4
ZojjV)O>qIH1/n[|2yE[>:i     "##%      ::##########"     eC97N-A&Kj_K_><wS5rtWk@
*a+Y5yH?b[F^e7C/56j|p    "##:         ###############"    mRe+:)BO98(Zh)'Iof*nm
.,$C5Nyt=PPu01Avw^<    "#            #.   .####:#######"    IiQ=5$'D-y?g6`YT+qL
w9k^ch|K'),tc6ygIL   "              ##### # :############"   8xI#LNz3v}T=4WlL27
FZ0ij)7TQCI)P7u}R   "              #######################"   T5-iJbbG5P-DHB<.R
,YvZ_rnv6ky-G+4U   "              ############:####  %#####"   '$*are@b4U351Q-u
g500x8RR%`Om7VD   "              .#############:##%   .##  ."   p4M5PFixrPvl&<p
[]1IJEGgDt8Lm#;  " %%            .################.     #.   "  bc4zS^y]0`_Pstf
UxOC(q/,}.YOIFj  ":####:          :##############%       :   "  (k&q_VzcaAi?]^l
CVYp''');v=([v,  "%######.              #########            "  ][0]-int(((sys)
.argv[1:]+[45,[  "##########.           #######%             "  ]])[0]))%360;s;
s=('v=%04o;'%v+  "###########           :######.             "  *0+'s=""'+'"'+s
+'""'+'";exe'+[  ":#########:           .######: .           "  ][0]*0+'c(s)');
d=[([ord(c)] or   " :#######%           :###### #:          "   )[0]for c in d]
f=lambda x,y:x*[   "  ######%           .####% ::          "   ,90][1]+(y-2)%91
t="%x"%reduce(f,[   "  ####%             %###             "   ,d][1],0);e=(zlib
.decompress);e=e([   " .###:             .#%             "   ,t.decode('hex')][
1]);j="".join;e=j((    " %##                           "    *0+"{0:08b}".format
(ord(b)))for b in e);    " #.                        "    ;s=list(s);z=360;p=(s
.__setitem__);q,_,r=[90,    " .                   "     ,range];[(lambda w=int(
(math.sqrt(1-((y*2.0-21)/22)**(2))*23)):[(lambda t=90*x/w+v+90: (lambda u=(e[y*z:(y+1)*z]*2)[t:t+90/w]:p((y*80)+120-w+x, " .:%#"[4 * u.count("0") / len(u)]))())() for x in range(w*2-1)])()for y in range(22)]







#for y in range(25):
#    print "".join(s[y*80:y*80+80])

print j(s)
# + "; _ The Qlobe#{" "*18+ ("Copyright(C).Yusuke Endoh, 2010")}";
""";exec(s)
