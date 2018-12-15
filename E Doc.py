from  easygui import *
import sys
name=enterbox("Please enter your name")
name1=str(name)
msgbox("Hello "+name1+" I am your Doctor assistant","E-DOCTOR")
message="select your symptom for your further  analysis of your problems"
titles="E-DOCTOR:YOUR PROFESSIONAL ASSISTANT"
symptom=["headache","cold","cough","body pains","vomiting","allergy"]
symptom1=choicebox(message,titles,symptom)
if symptom1=="headache":
       msg=("How long has this been troubling to you ")
       title=("E-DOCTOR :SYMPTOM=HEADACHE")
       choices=["Less than one day","One day to one week","One week to one month ","One month to one year"]
       choice= choicebox(msg,title,choices)
       if  choice =="less than one day"or"one day to one week":
           msg=("is your headache mainly located on one or both side of the head?")
           title=("E-DOCTOR:symptom=Headache")
           choices=["one side","both side"]
           choice=choicebox (msg,title, choices)
           if choice=="one side" or "both side":
             msg=("is it a throbbing headache?")
             title=("E-DOCTOR :symptom=Headache")
             choices=["Yes","No"]
             choice=choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                msg=("How does bending forward affect your headache?")
                title=("E-DOCTOR :symptom=Headache")
                choices=["Worsens","No effect"]
                choice=choicebox(msg,title,choices) 
                if choice=="Worsens"or "No effect ":
                   msg=("How would you describe the intensity of your headache?")
                   title=("E-DOCTOR :symptom=Headache")
                   choices=["Mild","Severe"]
                   choice=(choicebox, title,choices)
                   if choice =="Mild" or "Severe":
                      msg=("Did you suffer a head or neck injury before your first symptom occurred?")
                      title=("E-DOCTOR:symptom=Headache")
                      choices=["Yes","No"]
                      choice=choicebox(msg,title, choices) 
                      if choice =="Yes" or "No":
                         msg=("Do the symptoms occur in the days before your period starts?")
                         title=("E-DOCTOR:SYMPTOM HEADACHE")
                         choices=["Yes","No"]
                         choice=choicebox(msg,title,choices)
                         if choice=="Yes" or "No":
                            msg=("Have you recently had a long distance flight?")
                            title=("E-DOCTOR :symptom=Headache")
                            choices=["Yes","No"]
                            choice=choicebox(msg,title,choices)
                            if choice=="Yes" or "No":
                               msg=("is your scalp score when touched or pressed?")
                               title=("E-DOCTOR :symptom=Headache")
                               choices=["Yes","No"]
                               choice=choicebox(msg,title,choices)
                               if choice=="Yes" or "No":
                                  msg=("do you pain in the bones or skin around your eye socket?")
                                  title=("E-DOCTOR :symptom=Headache")
                                  choices=["Yes","No"]
                                  choice= choicebox(msg,title,choices)
                                  if choice=="Yes" or "No":
                                     msg=("do you have pain behind the eye?")
                                     title=("E-DOCTOR :symptom=Headache")
                                     choices=["Yes","No"]
                                     choice=choicebox(msg,title,choices)
                                     if choice=="Yes":
                                        msg=("do you have pain in the back of your neck?")
                                        title=("E-DOCTOR:symptom=Headache")
                                        choices=["Yes","No"]
                                        choice=choicebox(msg,title,choices)
                                        if Choice=="Yes" or "No":
                                           msg=("Causes of headache""\n:1.Brain Freeze","\n2.Stress","\n3.Dehydration","\n4.Stroke")
                                           title=("E- DOCTOR:SYMPTOM HEADACHE")
                                           choices=["I will prefer doctor","Medicines to prefer"]
                                           choice=choicebox(msg,title,choices)
                                           if choice=="I will prefer doctor":
                                              msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 
                                           elif choice=="Medicines to prefer":
                                                msg=("please select the preference")
                                                title=("E- DOCTOR:SYMPTOM HEADACHE")        
                                                choices=["Ayurvedic","Allopathic creams"]
                                                choice=choicebox(msg,title,choices)
                                                if choice=="Ayurvedic":
                                                   msgbox("1.Narikel Lavan,2.Sootshekhar Rasa,3.Sitopaladi Churna,4. Rason Vati,5.Godanti Mishra")
                                                   msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 
                                                elif choices=="Allopathic creams":
                                                     msgbox("1. Acetaminephen,2.Ibuprofen,3.Naproxen")
                                                     msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 


                                     elif choice=="No":
                                        msg=("do you have pain in the back of your neck?")
                                        title=("E-DOCTOR:symptom=Headache")
                                        choices=["Yes","No"]
                                        choice=choicebox(msg,title,choices)
                                        if choice=="Yes" or "No":
                                           msg=("Causes of headache""\n:1.Brain Freeze","\n2.Stress","\n3.Dehydration","\n4.Stroke")
                                           title=("E- DOCTOR:SYMPTOM HEADACHE")
                                           choices=["I will prefer doctor","Medicines to prefer"]
                                           choice=choicebox(msg,title,choices)
                                           if choice=="I will prefer doctor":
                                              msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 
                                           elif choice=="Medicines to prefer":
                                                msg=("please select the preference")
                                                title=("E- DOCTOR:SYMPTOM HEADACHE")        
                                                choices=["Ayurvedic","Allopathic creams"]
                                                choice=choicebox(msg,title,choices)
                                                if choice=="Ayurvedic":
                                                   msgbox("1.Narikel Lavan,2.Sootshekhar Rasa,3.Sitopaladi Churna,4. Rason Vati,5.Godanti Mishra")
                                                   msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 
                                                elif choices=="Allopathic creams":
                                                     msgbox("1. Acetaminephen,2.Ibuprofen,3.Naproxen")
                                                     msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ") 


elif symptom1=="cold":
          msg=("are you passing less urine than usual")
          title=("E-DOCTOR: SYMPTOME=COLD")
          choices=["yes","no"]
          choice=choicebox(msg,title,choices)
          if choices=="yes" or "no":
             msg=("Do you feel unsure about where are you")
             title=("E-DOCTOR: SYMPTOME=COLD")
             choices=["yes","no"]
             choice=choicebox(msg,title,choices)
             if choices=="yes "or "no":
                msg=("Is your pulse racing faster than normal limit")
                title=("E-DOCTOR: SYMPTOME=COLD")
                choices=["yes","no"]
                choice=choicebox(msg,title,choices)
                if choices=="yes" or "no":
                   msg=("are you breathing faster than usual")
                   title=("E-DOCTOR: SYMPTOME=COLD")
                   choices=["yes","no"]
                   choice=choicebox(msg,title,choices)
                   if choices=="yes" or "no":
                      msg=("Does your heartbeat feel different than usual")
                      title=("E-DOCTOR: SYMPTOME=COLD")
                      choices=["yes","no"]
                      choice=choicebox(msg,title,choices)
                      if choices=="yes" or "no":
                         msg=("Has your face become unusually pale")
                         title=("E-DOCTOR: SYMPTOME=COLD")
                         choices=["yes","no"]
                         choice=choicebox(msg,title,choices)
                         if choices=="yes" or "no":
                            msg=("Do you have reduced,distortd or blurred vision")
                            title=("E-DOCTOR: SYMPTOME=COLD")
                            choices=["yes","no"]
                            choice=choicebox(msg,title,choices)
                            if choices=="yes" or "no":
                               msg=("Did the change in vision happen suddenly")
                               title=("E-DOCTOR: SYMPTOME=COLD")
                               choices=["yes","no"]
                               choice=choicebox(msg,title,choices)
                               if choices=="yes" or "no":
                                  msg=("Have you lost your appetite")
                                  title=("E-DOCTOR: SYMPTOME=COLD")
                                  choices=["yes","no"]
                                  choice=choicebox(msg,title,choices)
                                  if choices=="yes" or "no":
                                     msg=("Are you feel agiated and physically restless")
                                     title=("E-DOCTOR: SYMPTOME=COLD")
                                     choices=["yes","no"]
                                     choice=choicebox(msg,title,choices)
                                     if choices=="yes" or "no":
                                        msg=("Do you feel dizzy")
                                        title=("E-DOCTOR: SYMPTOME=COLD")
                                        choices=["yes","no"]
                                        choice=choicebox(msg,title,choices)
                                        if choices=="yes" or "no":
                                           msg=("Are you feeling cold for no apparent reason")
                                           title=("E-DOCTOR: SYMPTOME=COLD")
                                           choices=["yes","no"]
                                           choice=choicebox(msg,title,choices)
                                           if choices=="yes" or "no":
                                              msg=("Do you have dry skin all over your body")
                                              title=("E-DOCTOR: SYMPTOME=COLD")
                                              choices=["yes","no"]
                                              choice=choicebox(msg,title,choices)
                                              if choices=="yes" or "no":
                                                 msg=("Are you sweating more than usual")
                                                 title=("E-DOCTOR: SYMPTOME=COLD")
                                                 choices=["yes","no"]
                                                 choice=choicebox(msg,title,choices)
                                                 if choices=="yes" or "no":
                                                    msg=("Are you having difficulty in breathing")
                                                    title=("E-DOCTOR: SYMPTOME=COLD")
                                                    choices=["yes","no"]
                                                    choice=choicebox(msg,title,choices)
                                                    if choice=="yes" or"no":
                                                       msg=("Causes for cold","\n 1.human parainfluenza virus","\n 2.Human metapneumovirus","\n 3.coronaviruses adenovirus","\n 4.human respiratory syncytial virus","\n 5. enteroviruses")
                                                       title=("E-DOCTOR: SYMPTOME=COLD")
                                                       choices=["I will prefer Doctor","Medicines to prefer"]
                                                       choice=choicebox(msg,title,choices)
                                                       if choice=="I will prefer Doctor":
                                                          msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")
                                                       elif choice=="Medicines to prefer":
                                                            msg=("Please select the preference")
                                                            title=("E-DOCTOR: SYMPTOME=COLD")
                                                            choices=("Allopathy","Ayurvedic")
                                                            choice=choicebox(msg,title,choices)
                                                            if choice=="Allopathy":
                                                               msgbox("1.Advill,2.Tylenon,3.Sudafed,4.Mucinex DM")
                                                               msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")
                                                            elif choice=="Ayurvedic":
                                                                 msgbox("1.HERBOfit,2.Huff n Kuff,3.HERBOkold")
                                                                 msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")
   

elif symptom1=="cough":
       msg=("How long has this been troubling to you ")
       title=("E-DOCTOR :SYMPTOM=COUGH")
       choices=["Less than one day","One day to one week","One week to one month ","One month to one year"]
       choice= choicebox(msg,title,choices)
       if choice=="Less than one day" or "One day to one week":
          msg=("Do you have a sore throat?")
          title=("E-DOCTOR: SYMPTOM=COUGH")
          choices=["Yes","No"]
          choice=choicebox(msg,title,choices)
          if choice=="Yes" or "No":
             msg=("Are you coughing up phl egm?")
             title=("E-DOCTOR:  SYMPTOM=COUGH")
             choices=["Yes","No"]
             choice=choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                msg=("Do you have a fever?")
                title=("E-DOCTOR:  SYMPTOM=COUGH")
                choices=["Yes","No"]
                choice=choicebox(msg,title,choices)
                if choice=="Yes" or "No":
                   msg=("Are you having difficultly breathing?")
                   title=("E-DOCTOR:  SYMPTOM=COUGH")
                   choices=["Yes","No"]
                   choice=choicebox(msg,title,choices)
                   if choice=="Yes" or "No":
                      msg=("Do you have sensation of lump in your throat?")
                      title=("E-DOCTOR:  SYMPTOM=COUGH")
                      choices=["Yes","No"]
                      choice=choicebox(msg,title,choices)
                      if choice=="Yes" or "No":
                         msg=("Do you have a chest pain?")
                         title=("E-DOCTOR:  SYMPTOM=COUGH")
                         choices=["Yes","No"]
                         choice=choicebox(msg,title,choices)
                         if choice=="Yes":
                            msg=("Where is the chest pain mainly located?")
                            title=("E-DOCTOR:  SYMPTOM=COUGH")
                            choices=["On one side of the chest","On both sides of the chest"]
                            choice=choicebox(msg,title,choices)
                         elif choice=="No":
                              msg=("Is your throat redder than usual?")
                              title=("E-DOCTOR:  SYMPTOM=COUGH")
                              choices=["Yes","No"]
                              choice=choicebox(msg,title,choices)
                              if choice=="Yes" or "No":
                                 msg=("Possible causes:","\n 1.cold","\n 2.flu","\n 3.smoking","\n 4.allergies" )
                                 title=("E-DOCTOR:  SYMPTOM=COUGH")
                                 choices=["Medicines to prefer","I will prefer doctor"]
                                 choice=choicebox(msg,title,choices)
                                 if choice=="I will prefer doctor":
                                    msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
   

                                 elif choice=="Medicines to prefer":
                                      msg=("Please select category")
                                      title=("E-DOCTOR:  SYMPTOM=COUGH")
                                      choices=["Allopathy","Ayurvedik"]
                                      choice=choicebox(msg,title,choices)
                                      if choice=="Allopathy":
                                         msgbox("1.benzonatate. 2. Cheratussin ac. 3.mucinex")
                                         msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
                                      elif choice=="Ayurvedik":
                                           msgbox("1.honey. 2.tulsi leaves. 3.licorice")
                                           msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
       elif choice=="One week to one month" or "One month to one year":
            msg=("Do you have a sore throat?")
            title=("E-DOCTOR: SYMPTOM=COUGH")
            choices=["Yes","No"]
            choice=choicebox(msg,title,choices)
            if choice=="Yes" or "No":
               msg=("Are you coughing up phl egm?")
               title=("E-DOCTOR:  SYMPTOM=COUGH")
               choices=["Yes","No"]
               choice=choicebox(msg,title,choices)
               if choice=="Yes" or "No":
                  msg=("Do you have a fever?")
                  title=("E-DOCTOR:  SYMPTOM=COUGH")
                  choices=["Yes","No"]
                  choice=choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("Are you having difficultly breathing?")
                     title=("E-DOCTOR:  SYMPTOM=COUGH")
                     choices=["Yes","No"]
                     choice=choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                        msg=("Do you have sensation of lump in your throat?")
                        title=("E-DOCTOR:  SYMPTOM=COUGH")
                        choices=["Yes","No"]
                        choice=choicebox(msg,title,choice)
                        if choice=="Yes" or "No":
                           msg=("Do you have a chest pain?")
                           title=("E-DOCTOR:  SYMPTOM=COUGH")
                           choices=["Yes","No"]
                           choice=choicebox(msg,title,choices)
                           if choice=="Yes":
                              msg=("Where is the chest pain mainly located?")
                              title=("E-DOCTOR:  SYMPTOM=COUGH")
                              choices=["On one side of the chest","On both sides of the chest"]
                              choice=choicebox(msg,title,choices)
                           elif choice=="No":
                                msg=("Is your throat redder than usual?")
                                title=("E-DOCTOR:  SYMPTOM=COUGH")
                                choices=["Yes","No"]
                                choice=choicebox(msg,title,choices)
                                if choice=="Yes" or "No":
                                   msg=("Possible causes:","\n 1.cold","\n 2.flu","\n 3.smoking","\n 4.allergies" )
                                   title=("E-DOCTOR:  SYMPTOM=COUGH")
                                   choices=["Medicines to prefer","I will prefer doctor"]
                                   choice=choicebox(msg,title,choices)
                                   if choice=="I will prefer doctor":
                                      msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
   

                                   elif choice=="Medicines to prefer":
                                        msg=("Please select category")
                                        title=("E-DOCTOR:  SYMPTOM=COUGH")
                                        choices=["Allopathy","Ayurvedik"]
                                        choice=choicebox(msg,title,choices)
                                        if choice=="Allopathy":
                                           msgbox("1.benzonatate. 2. Cheratussin ac. 3.mucinex")
                                           msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
                                        elif choice=="Ayurvedik":
                                             msgbox("1.honey. 2.tulsi leaves. 3.licorice")
                                             msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
                  
elif symptom1=="body pains":
       msg=("How long has this been troubling to you ")
       title=("E-DOCTOR :SYMPTOM=HEADACHE")
       choices=["Less than one day","One day to one week","One week to one month ","One month to one year"]
       choice= choicebox(msg,title,choices)
       if choice=="Less than one day" or "One day to one week":
          msg=("Do you have any other symtoms?")
          title=("E-DOCTOR: SYMPTOM=BODY PAIN")
          choices=["Yes","No"]
          choice=choicebox(msg,title,choices)
          if choice=="Yes" or "No":
             msg=("DO YOU HAVE A RUNNY NOSE?")
             title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
             choices=["Yes","No"]
             choice=choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                msg=("Do you have a fever?")
                title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                choices=["Yes","No"]
                choice=choicebox(msg,title,choices)
                if choice=="Yes" or "No":
                   msg=("ARE YOU FELLING COLD FOR NO APPRENT REASON?")
                   title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                   choices=["Yes","No"]
                   choice=choicebox(msg,title,choices)
                   if choice=="Yes" or "No":
                      msg=("Do you have A COUGH?")
                      title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                      choices=["Yes","No"]
                      choice=choicebox(msg,title,choices)
                      if choice=="Yes" or "No":
                         msg=("HAVE YOU LOST YOUR APPETITE?")
                         title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                         choices=["Yes","No"]
                         choice=choicebox(msg,title,choices)
                         if choice=="Yes":
                            msg=("DO YOU HAVE DIARRHOEA OR ARE YOUR STOOLS LOOSER THAN USUAL?")
                            title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                            choices=["Yes","No"]
                            choice=choicebox(msg,title,choices)
                            if choice=="Yes or No":
                                 msg=("Cause of body pains","\n1.Tension","\n2.Stress","\n3.Overuse ","\n4.Minor injuries")
                                 title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                 choices=["I will prefer doctor"," Medicines to prefer"]
                                 choice=choicebox(msg,title,choices)
                                 if choice=="I will prefer doctor":
                                    msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                                 elif choice=="Medicines to prefer":
                                      msg=("Please select category")
                                      title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                      choices=["Allopathy","Ayurvedik"]
                                      choice=choicebox(msg,title,choices)
                                      if choice=="Allopathy":
                                         msgbox("1.Essentiale L. 2. Darolac 3.Acetaminophen")
                                         msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                                      elif choice=="Ayurvedik":
                                           msgbox("1.Shatavari. 2.ginger. 3.Turmeric")
                                           msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                         elif choice=="No":
                              msg=("Is your throat redder than usual?")
                              title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                              choices=["Yes","No"]
                              choice=choicebox(msg,title,choices)
                              if choice=="Yes" or "No":
                                 msg=("Cause of body pains","\n1.Tension","\n2.Stress","\n3.Overuse ","\n4.Minor injuries")
                                 title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                 choices=["I will prefer doctor","Medicines to prefer"]
                                 choice=choicebox(msg,title,choices)
                                 if choice=="I will prefer doctor":
                                    msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                                 elif choice=="Medicines to prefer":
                                      msg=("Please select category")
                                      title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                      choices=["Allopathy","Ayurvedik"]
                                      choice=choicebox(msg,title,choices)
                                      if choice=="Allopathy":
                                         msgbox("1.Essentiale L. 2. Darolac 3.Acetaminophen")
                                         msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                                      elif choice=="Ayurvedik":
                                           msgbox("1.Shatavari. 2.ginger. 3.Turmeric")
                                           msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
       elif choice=="One week to one month" or "One month to one year":
            msg=("Do you have a sore throat?")
            title=("E-DOCTOR: SYMPTOM=BODY PAIN")
            choices=["Yes","No"]
            choice=choicebox(msg,title,choices)
            if choice=="Yes" or "No":
               msg=("HAVE YOU EVER HAD POLIO?")
               title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
               choices=["Yes","No"]
               choice=choicebox(msg,title,choices)
               if choice=="Yes" or "No":
                  msg=("Do you have joint pain in several different parts of your body at once?")
                  title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                  choices=["Yes","No"]
                  choice=choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("DO YOU FEEL EXTREMLY EXHAUSTED?")
                     title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                     choices=["Yes","No"]
                     choice=choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                        msg=("Do you have A COUGH?")
                        title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                        choices=["Yes","No"]
                        choice=choicebox(msg,title,choice)
                        if choice=="Yes" or "No":
                           msg=("IS YOUR SKIN EXTREMELY STRETCHY?")
                           title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                           choices=["Yes","No"]
                           choice=choicebox(msg,title,choices)
                           if choice=="Yes":
                              msg=("ARE YOU ABLE TO MOVE YOUR JOINTS FURTHER THAN THE NORMAL RANGE OF MOTION?")
                              title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                              choices=["Yes","No"]
                              choice=choicebox(msg,title,choices)
                           elif choice=="No":
                                msg=("have you been sleeping for more hours per than usual?")
                                title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                choices=["Yes","No"]
                                choice=choicebox(msg,title,choices)
                                if choice=="Yes" or "No":
                                   msg=("DO YOU HAVE A RUNNY NOSE?" )
                                   title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                   choices=["Yes","No"]
                                   choice=choicebox(msg,title,choices)
                                   if choice=="I will prefer doctor":
                                      msgbox("Your analysis is done. You have an acute cough. It can be cleared at home. You can use home  remedies to recover from it")
                                   elif choice=="Medicines to prefer":
                                        msg=("Please select category")
                                        title=("E-DOCTOR:  SYMPTOM=BODY PAIN")
                                        choices=["Allopathy","Ayurvedik"]
                                        choice=choicebox(msg,title,choices)
                                        if choice=="Allopathy":
                                           msgbox("1.Essentiate. 2.darolac.acetaminophen")
                                           msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
                                        elif choice=="Ayurvedik":
                                             msgbox("1.Shatavati 2.ginger. 3.Turmeric")
                                             msgbox("Your analysis is done. You have an acute body pain. It can be cleared at home. You can use home  remedies to recover from it")
elif symptom1=="vomiting":
       msg=("How long has this been troubling to you ")
       title=("E-DOCTOR :SYMPTOM=VOMITING")
       choices=["Less than one day","One day to one week","One week to one month ","One month to one year"]
       choice=choicebox(msg,titles,choices)
       if choice=="Less than one day" or "One day to one week":
             msg=("Do you have to throw up when drinking even small amounts of fluids")
             title=("E-DOCTOR :SYMPTOM=VOMITING")
             choices=["Yes","No"]
             choice= choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                  msg=("Have you been vomiting extremely forcefully")
                  title=("E-DOCTOR :SYMPTOM=VOMITING")
                  choices=["Yes","No"]
                  choice= choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("Have you taken more than the recommended dose of acetaminophen/paracetamol in the last three days")
                     title=("E-DOCTOR :SYMPTOM=VOMITING")
                     choices=["Yes","No"]
                     choice= choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                        msg=("Do you have diarrhoea or are your stools looser than usual")
                        title=("E-DOCTOR :SYMPTOM=VOMITING")
                        choices=["Yes","No"]
                        choice= choicebox(msg,title,choices)
                        if choice=="Yes" or "No":
                           msg=("Do you have abdominal pain")
                           title=("E-DOCTOR :SYMPTOM=VOMITING")
                           choices=["Yes","No"]
                           choice= choicebox(msg,title,choices)
                           if choice=="Yes":
                              msg=("where is the pain located within your abdomen?")
                              title=("E-DOCTOR :SYMPTOM=VOMITING")
                              choices=["All over Abdomen","In a specific part of abdomen"]
                              choice=choicebox(msg,title,choices)
                           elif choice=="No":
                                msg=("Do you have chest pain")
                                title=("E-DOCTOR :SYMPTOM=VOMITING")
                                choices=["Yes","No"]
                                choice= choicebox(msg,title,choices)
                                if choice=="Yes" or "No":
                                    msg=("Possible causes" ,"\n 1: Small bowel obstruction","\n 2: food allergy","\n 3: Viral stomach bug in adults")
                                    title=("E-DOCTOR : RESULTS")
                                    choices=["Medicines to prefer", "I will prefer doctor"]
                                    choice=choicebox(msg,title,choices)
                                    if choice=="I will prefer doctor":
                                       msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")
                                    elif choice=="Medicines to prefer":
                                         msg=("Please select category")
                                         title=("E-DOCTOR : RESULTS")
                                         choices=["Allopathy","Ayurveda"]
                                         choice=choicebox(msg,title,choices)
                                    if choice=="Allopathy":
                                       msgbox("1:Meclizine hydrochloride,2: Dimenhydrinate,3:Emetrol")
                                       msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")       
                                    elif choice=="Ayurveda":
                                         msgbox("1:Lime, 2: Cardomom, 3:Ginger, 4:Cumin tea helps in reducing vomiting")
                                         msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")       
       elif choice=="One week to one month" or "One month to one year":
             msg=("Do you have to throw up when drinking even small amounts of fluids")
             title=("E-DOCTOR :SYMPTOM=VOMITING")
             choices=["Yes","No"]
             choice= choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                  msg=("Have you been vomiting extremely forcefully")
                  title=("E-DOCTOR :SYMPTOM=VOMITING")
                  choices=["Yes","No"]
                  choice= choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("Have you taken more than the recommended dose of acetaminophen/paracetamol in the last three days")
                     title=("E-DOCTOR :SYMPTOM=VOMITING")
                     choices=["Yes","No"]
                     choice= choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                        msg=("Do you have diarrhoea or are your stools looser than usual")
                        title=("E-DOCTOR :SYMPTOM=VOMITING")
                        choices=["Yes","No"]
                        choice= choicebox(msg,title,choices)
                        if choice=="Yes" or "No":
                           msg=("Do you have abdominal pain")
                           title=("E-DOCTOR :SYMPTOM=VOMITING")
                           choices=["Yes","No"]
                           choice= choicebox(msg,title,choices)
                           if choice=="Yes":
                              msg=("where is the pain located within your abdomen?")
                              title=("E-DOCTOR :SYMPTOM=VOMITING")
                              choices=["All over Abdomen","In a specific part of abdomen"]
                              choice=choicebox(msg,title,choices)
                           elif choice=="No":
                                msg=("Do you have chest pain")
                                title=("E-DOCTOR :SYMPTOM=VOMITING")
                                choices=["Yes","No"]
                                choice= choicebox(msg,title,choices)
                                if choice=="Yes" or "No":
                                    msg=("Possible causes" ,"\n 1: Small bowel obstruction","\n 2: food allergy","\n 3: Viral stomach bug in adults")
                                    title=("E-DOCTOR : RESULTS")
                                    choices=["Medicines to prefer", "I will prefer doctor"]
                                    choice=choicebox(msg,title,choices)
                                    if choice=="I will prefer doctor":
                                       msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")
                                    elif choice=="Medicines to prefer":
                                         msg=("Please select category")
                                         title=("E-DOCTOR : RESULTS")
                                         choices=["Allopathy","Ayurveda"]
                                         choice=choicebox(msg,title,choices)
                                    if choice=="Allopathy":
                                       msgbox("1:Meclizine hydrochloride,2: Dimenhydrinate,3:Emetrol")
                                       msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")       
                                    elif choice=="Ayurveda":
                                         msgbox("1:Lime, 2: Cardomom, 3:Ginger, 4:Cumin tea helps in reducing vomiting")
                                         msgbox(" Hope our analysis helped you . Please remember AYURVEDIC OR HOMEOPATHY ARE VERY MUCH BETTER THAN ALLOPATHY ")       
elif symptom1=="allergy":
       msg=("How long has this been troubling to you ")
       title=("E-DOCTOR :SYMPTOM=ALLERGY")
       choices=["Less than one day","One day to one week","One week to one month ","One month to one year"]
       choice=choicebox(msg,titles,choices)
       if choice=="Less than one day" or "One day to one week":
             msg=("Have you recently spent time in direct sunlight or experienced hot weather ?")
             title=("E-DOCTOR :SYMPTOM=ALLERGY")
             choices=["Yes","No"]
             choice= choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                  msg=("Do you have one or more spots on any part of your face ?")
                  title=("E-DOCTOR :SYMPTOM=ALLERGY")
                  choices=["Yes","No"]
                  choice= choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("Does the skin of your cheeks appear reddened ?")
                     title=("E-DOCTOR :SYMPTOM=ALLERGY")
                     choices=["Yes","No"]
                     choice=choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                       msg=("Do you have scaly skin on any part of your face ?")
                       title=("E-DOCTOR :SYMPTOM=ALLERGY")
                       choices=["Yes","No"]
                       choice= choicebox(msg,title,choices)
                       if choice=="Yes" or "No":
                          msg=("Does your neck appear especially reddened ?")
                          title=("E-DOCTOR :SYMPTOM=ALLERGY")
                          choices=["Yes","No"]
                          choice= choicebox(msg,title,choices)
                          if choice=="Yes":
                             msg=("Is your reddened skin painful?")
                             title=("E-DOCTOR :SYMPTOM=ALLERGY")
                             choices=["Yes,too much","No, too little"]
                             choice=choicebox(msg,title,choices)
                          elif choice=="No":
                               msg=("Do you have pimples on any part of your face ?")
                               title=("E-DOCTOR :SYMPTOM=ALLERGY")
                               choices=["Yes","No"]
                               choice= choicebox(msg,title,choices)
                               if choice=="Yes" or "No":
                                  msg=("Possible causes" ,"\n 1: Race (Your skin color)","\n 2: Taking unprescribed medications","\n 3: Having blood relatives with similar kind of allergy")
                                  title=("E-DOCTOR : RESULTS")
                                  choices=["Medicines to prefer", "I will prefer doctor"]
                                  choice=choicebox(msg,title,choices)
                                  if choice=="I will prefer doctor":
                                     msgbox(" Hope our analysis helped you . Please remember, applying skin moisturizers and soothing skin remedies are the basic and the most helpfull ways to avoid the Allergy ")
                                  elif choice=="Medicines to prefer":
                                       msg=("Please select category")
                                       title=("E-DOCTOR : RESULTS")
                                       choices=["Creams","Ointments"]
                                       choice=choicebox(msg,title,choices)
                                       if choice=="Creams":
                                          msgbox("1:Hydrocortisone cream,2:Benadryl,3:Cortizone")
                                          msgbox(" Hope our analysis helped you . Please remember, applying skin moisturizers and soothing skin remedies are the basic and the most helpfull ways to avoid the Allergy ")
                                       elif choice=="Ointments":
                                            msgbox("1:Calamine lotion, 2:Antihistamines, 3:Aclovate Ointment")
                                            msgbox(" Hope our analysis helped you . Please remember, applying skin moisturizers and soothing skin remedies are the basic and the most helpfull ways to avoid the Allergy ")       
       elif choice=="One week to one month" or "One month to one year":
             msg=("Have you recently spent time in direct sunlight or experienced hot weather ?")
             title=("E-DOCTOR :SYMPTOM=ALLERGY")
             choices=["Yes","No"]
             choice= choicebox(msg,title,choices)
             if choice=="Yes" or "No":
                  msg=("Do you have one or more spots on any part of your face ?")
                  title=("E-DOCTOR :SYMPTOM=ALLERGY")
                  choices=["Yes","No"]
                  choice= choicebox(msg,title,choices)
                  if choice=="Yes" or "No":
                     msg=("Does the skin of your cheeks appear reddened ?")
                     title=("E-DOCTOR :SYMPTOM=ALLERGY")
                     choices=["Yes","No"]
                     choice=choicebox(msg,title,choices)
                     if choice=="Yes" or "No":
                       msg=("Do you have scaly skin on any part of your face ?")
                       title=("E-DOCTOR :SYMPTOM=ALLERGY")
                       choices=["Yes","No"]
                       choice= choicebox(msg,title,choices)
                       if choice=="Yes" or "No":
                          msg=("Does your neck appear especially reddened ?")
                          title=("E-DOCTOR :SYMPTOM=ALLERGY")
                          choices=["Yes","No"]
                          choice= choicebox(msg,title,choices)
                          if choice=="Yes":
                             msg=("Is your reddened skin painful?")
                             title=("E-DOCTOR :SYMPTOM=ALLERGY")
                             choices=["Yes,too much","No, too little"]
                             choice=choicebox(msg,title,choices)
                          elif choice=="No":
                               msg=("Do you have pimples on any part of your face ?")
                               title=("E-DOCTOR :SYMPTOM=ALLERGY")
                               choices=["Yes","No"]
                               choice= choicebox(msg,title,choices)
                               if choice=="Yes" or "No":
                                  msg=("Possible causes" ,"\n 1: Race (Your skin color)","\n 2: Taking unprescribed medications","\n 3: Having blood relatives with similar kind of allergy")
                                  title=("E-DOCTOR : RESULTS")
                                  choices=["Medicines to prefer", "I will prefer doctor"]
                                  choice=choicebox(msg,title,choices)
                                  if choice=="I will prefer doctor":
                                     msgbox(" Hope our analysis helped you . Please remember, applying skin moisturizers and soothing skin remedies are the basic and the most helpfull ways to avoid the Allergy ")
                                  elif choice=="Medicines to prefer":
                                       msg=("Please select category")
                                       title=("E-DOCTOR : RESULTS")
                                       choices=["Creams","Ointments"]
                                       choice=choicebox(msg,title,choices)
                                       if choice=="Creams":
                                          msgbox("1:Hydrocortisone cream,2:Benadryl,3:Cortizone")
                                       elif choice=="Ointments":
                                            msgbox("1:Calamine lotion, 2:Antihistamines, 3:Aclovate Ointment")
                                            msgbox(" Hope our analysis helped you . Please remember, applying skin moisturizers and soothing skin remedies are the basic and the most helpfull ways to avoid the Allergy ")  