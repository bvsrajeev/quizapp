import os
import shutil
def prev_que(lq,qno):
    if(qno == 1):
        return str(qno)+'.html'
    return str(qno-1)+'.html'
def next_que(lq,qno):
    if(qno == len(lq)):
        return str(qno)+'.html'
    return str(qno+1)+'.html'
def find_img(que,q):
    if('@' not in que):
        return que
    if(q == 0):
        return "<img class = img-medium src = '"+que[1:]+"';>"
    words = que.split(' ')
    end = None
    if(not words[-1][-1].isalpha()):
        end = words[-1][-1]
        words[-1] = words[-1][:-1]
    ind = 0
    for word in words:
        if(word[0] == '@'):
            word = word[1:]
            word = "<br><img class = img-medium src = "+word+";><br><br>"
            words[ind] = word
        ind+=1
    return ' '.join(words)
html1 = """<html>
  <head>
<link rel="stylesheet" href="style.css">
<script type="text/javascript" src="main.js">
</script>
<script>
function answer(){
  var answer ="""
#answer=que_op[-1]
html2 = """return answer;
}
function show_it(i){
  if(i == answer())
  {
    paint = '#008000';
    //console.log("green");
    var a = document.getElementById("correct")
    a.play();
  }
  else
  {
    paint = '#ff0000';
    //console.log("red");
    var a = document.getElementById("wrong");
    a.play();
  }
  var o = document.getElementById(i);
  o.style.backgroundColor = paint;
  return;
}
</script>
  </head>
  <body>
  <audio id="correct">
    <source src="correct.mp3" type="audio/mpeg">
  </audio>
  <audio id="wrong">
    <source src="wrong.mp3" type="audio/mpeg">
  </audio>

      <div class="center text-big ">"""
#que_op[0]
html3 = """</div>;
<button class="opt-button" onclick = "show_it('1')" id = "1">"""
#que_op[1]
html4="""</button>
<button class="opt-button" onclick = "show_it('2')" id = "2">"""
#que_op[2]
html5="""</button><br>
<button class="opt-button" onclick = "show_it('3')" id = "3">"""
#que_op[3]
html6="""</button>
<button class="opt-button" onclick = "show_it('4')" id = "4">"""
#que_op[4]
html7 = """</button>
<br><br>
<div align='center'>
<a href="""
#prev_que(lq,i)
html8 = """>
<input type="submit" class="button" value="prev Question"></a>
<a href="""
#next_que(lq,i)
html9 = """>
<input type="submit" class="button" value="Next Question"></a>
</div>
</body>
</html>"""
file = input('enter file name\n')
#file += '.txt'
fin = open(file+'.txt','r')
questions = fin.read()
fin.close()
print(questions)
lq = questions.split('\n')
try:
    os.mkdir(file)
except:
    pass
shutil.copy('essential/style.css',file+'/style.css')
shutil.copy('essential/wrong.mp3',file+'/wrong.mp3')
shutil.copy('essential/correct.mp3',file+'/correct.mp3')
#lq = lq[1:-1]
print(lq)
qno = 0;
for que in lq:
    if(not que or que == '\n'):
        continue
    qno += 1
    que_op = que.split('$')
    print(que_op)
    html_1 = html1+que_op[-1]+';'+html2+find_img(que_op[0],1)+html3+find_img(que_op[1],0)+html4+find_img(que_op[2],0)+html5+find_img(que_op[3],0)+html6+find_img(que_op[4],0)
    html_2 = html7+str(prev_que(lq,qno))+html8+str(next_que(lq,qno))+html9
    fname = file+'/'+str(qno)+'.html'
    fout = open(fname,'w+')
    fout.write(html_1+html_2)
    fout.close()
print("operation complete!!!!")

