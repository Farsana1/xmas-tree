print('MERRY CHRISTMAS')
print('\n \n')
z = 30
x = 1
for i in range(23):
  if( z > x ):
        print(' ' * z + '*' * x + ' ' * z)
  elif( x > z ):
        print(' ' * z + ' ' * x + ' ' * z)
  x+=2
  z-=1
