import sys

error = 'hanoi.error'

def moveit(frm, to):
   print 'move %s --> %s' % (frm, to)

def dohanoi(n, to, frm, using):
   if n == 0: return []
   dohanoi(n-1, using, frm, to);
   moveit(frm, to);
   dohanoi(n-1, to, using, frm);

def main():
   if len(sys.argv) > 1:
      for arg in sys.argv[1:]:
         n = eval(arg)
         dohanoi(n, 3, 1, 2)
   else:
      try:
         while 1:
            n = input()
            dohanoi(n, 3, 1, 2)
      except EOFError:
         pass
