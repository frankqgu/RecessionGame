def main():
  print("Frank Gu's Investment Game!")
  print("===========================================")
  print("Instructions: Type A) or B) etc. whenever prompted\n")
  game()

def game():
  Answer = (input("This game focuses on playing as a character from the 2008 era. It puts into perspective real scenarios that citizens were presented with. Would you like to play as \n A) A Collge Student Looking For A Car \n B) Mother Starting Her Kid's College Savings In The Stock Market \n C) Recent Immagrant looking for a home \nEnter A or B or C:"))

  if Answer == ("A"): 
    print("Recently, there has been a huge boom in popularity for SUVS and Pickup Trucks. 'An SUV Craze' as American Companys such as Ford, Dodge, and General Motors are heavily promoting more larger cars over compact ")
    print("But More Asian Manufactures are still developing compact size cars. In this case, which type of cars would you like? ")
    Answer = (input("\n A) Go with the American brands like Ford, Dodge, and Chevrolet and buy a Large Sedan/SUV \n B) Go with an oversea brand like Honda, Hyundai-Kia, and Nissan and buy a subompact \nEnter A) or B):"))
    if Answer == ("A"): 
      print("Well, atleast you got yourself a higher end car...right?")
      print("Yikes, as a college student, you do not have enough cash in hand to buy car. Meaning you need to take out a car loan! It just so happens that the people who give out payment plans and leases (aka.captive lessors) are hit in a wave of recession. They are hit even harder than regular banks because they don't have Demand Deposit cash to fall back on!")
      Answer = (input("Wait, luckily for you, Chrysler, one of the top 3 car companies just filed for bankruptcy. Hundreds of Thousands of trucks and SUVs are stuck with nowhere else to go with a new enviromental conscience movement picking up alongside the recession. GM is now looking for bailouts and already prices are dropping around the board. You got an offer for 50% off on a new Jeep, do you take it?\nEnter Yes) or No):"))
      if Answer == ("Yes"):
        print("Unfortunatly for you, the petrol prices of the car rises the highest it has even been in history. Up to $4.1 in june of 2008 from just $3 in February. This is due to other nations scaling their prices up from the market set value, countries like China who overscales the price by 41% of global average, drinving the prices up. You have made a great investment on your car, now you have stumbled across one of the worst times to use it. The insurance selection are stricter than ever as people are ever more considerate of their credit. After all, it's untrustworthy borrowers who started this recession in the first place. On the flip side, at least you were able to get a car before the recession set in. or else no one would accept your credit as a fresh student.  ")
        (input("Game Over!\n\nEnter N) for New Game:"))
        if Answer == ("N)"): 
          main()
        else: 
          print("Good Bye!")
      elif Answer == ("No"):
        print("It turns out, Chrysler, the parent company of Jeep, was defaulting on over $4 billion in secured debts. The auto contracts and leases were lesser and lesser in value, leading to more and more vacant cars. Thus why they wanted to get rid of the cars before they file for bankruptcy, which, they did in early 2009. The US Treasury, through the Troubled Asset Relief Program, invested $12.5 billion in Chrysler and recovered $11.2 billion when the company shares were sold in May 2011, resulting in a $1.3 billion loss. Your jeep certainly will have to wait quite a while for it's value to climb back up!")
        (input("Game Over!\n\nEnter N) for New Game:"))
        if Answer == ("N)"): 
          main()
        else: 
          print("Good Bye!")

        
    elif Answer == ("B"):
      print("The auto companies in Asian countries are known for their more efficient work forces and costs. By getting a car from them, you contribute in further exposing the weakness of the American auto manufacturing: US Companies are pushing more for disel and heavier load automobiles in order to turn a profit. They cannot get profit if they sell compact and smaller sedans. So they try and cut corners eleswhere...")
      Answer = (input("Wow, it looks like the workers are getting sick of their treatment in the US workplaces too. They are holding a strike against the Big 3, and they have been pretty successful in it. The strike eventually reaches your workplace, and your workplace has to close admist of the protest. You are laid off. Do you:\n A) Pawn in your car in joining the protests and look for a better one down the road \n B) Stick with the subcompact car and hope it's more efficent \nEnter A or B:"))
      if Answer == ("A"):
        print("Perfect timing! In midst of the recession, Hyundai-KIA, South Korean auto giant and your subcompact car's brand, offered a special deal to it's customers:If they lost their income within 1 year of buying/leasing the car, they can return the car for no reprecussions and a full refund to help them. You happily take the money, as recession continues, worries about deflation becomes a serious concern, and you know that this grand amount of money in this state will help sustain you very well. ")
        (input("Game Over!\n\nEnter N) for New Game:"))
        if Answer == ("N)"): 
          main()
        else: 
          print("Good Bye!")
          
      elif Answer == ("B"):
        print("The value you waited for eventually came. The 2008 financial crisis and Great Recession induced a bear market in oil and gas, sending the price of a barrel of crude oil from $133.88 to $39.09 in just a less than a year. This is due to a low demand, and even less in regular fuel as many were switched to disel fuel. Cheap gas! yay!")
        (input("Game Over!\n\nEnter N) for New Game:"))
        if Answer == ("N)"): 
          main()
        else: 
          print("Good Bye!")
    
  else: 
    if Answer == ("B"): 
      print("")
      end
def player_died():
  print("You died, the bear eventually ate you...")
  Answer = (input("Game Over!\n\nEnter N) for New Game:"))
  if Answer == ("N)"): 
    main()
  else: 
    print("Good Bye!")

def player_ran():
  Answer = (input("You find an exit from the forest, what do you do\n A) Exit forest\n B) Run around in forest \nEnter A) or B):")) 
  if Answer == ("A)"): 
    print("You exited the forest")
    player_crossedRoad()
  else: 
    print("You (although insanly) chose to run around in the forest") 
    player_stillRunsinForest()

def player_crossedRoad():
  print("You get the idea...")

main ()
