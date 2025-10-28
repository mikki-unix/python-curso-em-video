from time import sleep

cardinais = [
  'ZERO!', 'UM!', 'DOIS!', 'TRÊS!', 'QUATRO!', 'CINCO!', 'SEIS!', 'SETE!', 'OITO!', 'NOVE!', 'DEZ!'
]

for i in range(10, -1, -1):
  print(cardinais[i].capitalize())
  sleep(1)

print("""
                                   .''.       
       .''.      .        *''*    :_\/_:     . 
      :_\/_:   _\(/_  .:.*_\/_*   : /\ :  .'.:.'.
  .''.: /\ :   ./)\   ':'* /\ * :  '..'.  -=:o:=-
 :_\/_:'.:::.    ' *''*    * '.\'/.' _\(/_'.':'.'
 : /\ : :::::     *_\/_*     -= o =-  /)\    '  *
  '..'  ':::'     * /\ *     .'/.\'.   '
      *            *..*         :
        *
        *
""")
