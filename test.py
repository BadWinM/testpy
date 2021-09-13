message['Date'] = f_time[0] + ', ' + f_time[2] + ' ' + f_time[1] + ' ' + f_time[4] + ' ' + f_time[3] + ' +0100' + '\r\n'
if nature == 'registration':
    message['Subject'] = "inscription"
    msg = "Bomjour, " + session['user']['name'] + " merci de valider votre inscription  en cliquant sur  ce lien " + lien 
elif nature == 'password':
    message['Subject'] = "Reinitialisation du mot de passe" 
    msg = "Bomjour, merci de suivre ce lien pour réinitialiser votre mot de passe " + lien
elif nature == 'fake':
    message['Subject'] = "Declaration de faux compte" 
    user = session['user']['name']
    fake = unique
    msg = "l'utilisateur " + user + " a indiqué que le compte " + fake + ' est un faux'
message.attach(MIMEText(msg.encode('utf-8'), 'plain', 'utf-8'))  
serveur = smtplib.SMTP('mail.infomaniak.com', 587)  # # Connexion au serveur sortant 
serveur.starttls()  # # Spécification de la sécurisation

serveur.login("jiasdlj", "coucoubg")

def coordonnees(c):  # separe latitude et longitude  
    debut = c.find('(')
    virgule = c.find(',')
    fin = c.find(')')
    lat = c[debut + 1:virgule]
    lon = c[virgule + 1:fin]
    coor = (lat, lon)
    return (coor)