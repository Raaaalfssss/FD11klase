#ralfsViļumsons 11.b klase (18.10)

password= ("python123") 
#password norāda pareizo paroli
guess = (input("Ievadi paroli"))
#guess ļauj minētn un input ļauj ievadīt paroli
while guess != password:
#while ir nepārtraukts cikls kamēr notiek darbība
    if guess > password:
        print("Piekļuve liegta!")
    elif guess < password:
        print("Piekļuve liegta!")
    guess = (input("mēgini vēlreiz"))
#ja ievadītā parole ir kļūdaina vai nepareiza, tas tiek norādīts un to var ievadīt atkārtoti
if guess == password:
        print("Piekļuve atļauta!")
#ja parole tiek ievadīta pareizi tad cikls noslēdzas
#es šo visu saprotu, bet nemāku izskaidrot