


def __calculate():

    distance=156

    # get the selected mode from the dropdown 
    mode='Car'
    # price=0
    uniprice=0

    if(mode=='Car'):
      uniprice=50
    elif (mode=='Bus'):
      uniprice=100
    else:
      uniprice=150

    if(uniprice<=0):
      print('wrong price')
    else:
      total=float(distance)*uniprice

      
