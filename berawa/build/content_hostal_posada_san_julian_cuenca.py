# Contenido de la demo Posada San Julián (Cuenca) (es/en/fr/de). Hechos de posadasanjulian.es leidos el 02/11/2026 (ver berawa/sources.json). Sin precios ni valoraciones.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran el alojamiento real.','en':' Images are illustrations and do not show the actual property.','fr':' Les images sont des illustrations et ne montrent pas l’établissement réel.','de':' Die Bilder sind Illustrationen und zeigen nicht die tatsächliche Unterkunft.'}
H={'es':['Habitación individual','Habitación doble','Habitación familiar'],'en':['Single room','Double room','Family room'],'fr':['Chambre individuelle','Chambre double','Chambre familiale'],'de':['Einzelzimmer','Doppelzimmer','Familienzimmer']}
RD={
'es':['Dos habitaciones individuales, con baño privado, calefacción central y televisión.','Diez habitaciones dobles, con baño privado, calefacción central, televisión y wifi gratuito.','Cuatro habitaciones familiares para 3 o 4 personas, con baño privado, calefacción y televisión.'],
'en':['Two single rooms, with private bathroom, central heating and television.','Ten double rooms, with private bathroom, central heating, television and free wifi.','Four family rooms for 3 or 4 people, with private bathroom, heating and television.'],
'fr':['Deux chambres individuelles, avec salle de bains privée, chauffage central et télévision.','Dix chambres doubles, avec salle de bains privée, chauffage central, télévision et wifi gratuit.','Quatre chambres familiales pour 3 ou 4 personnes, avec salle de bains privée, chauffage et télévision.'],
'de':['Zwei Einzelzimmer mit eigenem Bad, Zentralheizung und Fernseher.','Zehn Doppelzimmer mit eigenem Bad, Zentralheizung, Fernseher und kostenlosem WLAN.','Vier Familienzimmer für 3 oder 4 Personen mit eigenem Bad, Heizung und Fernseher.']}
ART={
'hero':('arches',1911,['#2a1d17','#8a5a3c','#f3e6d6','#6b4a36','#4a3427','#1c1410']),
'intro':('columns',1912,['#f6f2ea','#fbf9f4','#8a4b2a','#5f5850','#2e2a25']),
'r1':('arches',1921,['#2a1d17','#9a6a4a','#f5ebde','#76523c','#55392b','#1c1410']),
'r2':('skyline',1922,['#f6f2ea','#fbf9f4','#8a4b2a','#5f5850','#2e2a25']),
'r3':('hills',1923,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g1':('skyline',1931,['#2a1d17','#8a5a3c','#f3e6d6','#6b4a36','#4a3427','#1c1410']),
'g2':('hills',1932,['#f4efe4','#e8dcc4','#c9a87a','#9a8062','#735f48','#4b3d2f']),
'g3':('arches',1933,['#2a1d17','#9a6a4a','#f5ebde','#76523c','#55392b','#1c1410']),
'g4':('columns',1934,['#f6f2ea','#fbf9f4','#8a4b2a','#5f5850','#2e2a25'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='Posada San Julián · Hostal y restaurante en Cuenca',see_rooms='Ver habitaciones',hero_k='Cuenca · Calle Torres, 1',hero_t='Hostal familiar en el centro de Cuenca',hero_s='Una casa histórica del siglo XVI, a un paso de las Casas Colgadas y del casco antiguo.',
 intro_t='Hospedaje de tradición familiar desde 1966',intro_p1='En septiembre de 1966 Virgilio Álvarez y Albina Collado abrieron el negocio; hoy lo lleva una de sus hijas.',
 intro_p2='El edificio, con un balcón de esquina renacentista, fue declarado bien de interés cultural en 1999.',
 stats=['16 habitaciones','Bien de interés cultural','Restaurante propio','Wifi gratuito'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Todas con baño privado, calefacción central y televisión. Hay también algunas habitaciones más pequeñas con lavabo y baño completo en el pasillo.',
 svcs=['Restaurante de cocina tradicional','Menú del día','Dos comedores para celebraciones','Wifi gratuito','Aparcamiento público a 2 minutos a pie','Información de alérgenos'],
 loc_p='Calle Torres, 1 · 16001 Cuenca. Teléfono: 969 211 704. Correo: info@posadasanjulian.es.',
 chips=['¿Qué habitaciones tenéis?','¿Hay desayuno?','¿Dónde aparco?','¿Cómo reservo?']),
'en':dict(title='Posada San Julián · Guesthouse and restaurant in Cuenca',see_rooms='See rooms',hero_k='Cuenca · Calle Torres, 1',hero_t='A family guesthouse in the centre of Cuenca',hero_s='A 16th-century historic house, a short walk from the Hanging Houses and the old town.',
 intro_t='Family hospitality since 1966',intro_p1='In September 1966 Virgilio Álvarez and Albina Collado opened the business; today one of their daughters runs it.',
 intro_p2='The building, with a Renaissance corner balcony, was declared a site of cultural interest in 1999.',
 stats=['16 rooms','Site of cultural interest','Own restaurant','Free wifi'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='All with private bathroom, central heating and television. There are also some smaller rooms with a washbasin and a full bathroom in the corridor.',
 svcs=['Traditional cuisine restaurant','Daily set menu','Two dining rooms for celebrations','Free wifi','Public car park 2 minutes on foot','Allergen information'],
 loc_p='Calle Torres, 1 · 16001 Cuenca. Phone: +34 969 211 704. Email: info@posadasanjulian.es.',
 chips=['Which rooms do you have?','Is there breakfast?','Where can I park?','How do I book?']),
'fr':dict(title='Posada San Julián · Pension et restaurant à Cuenca',see_rooms='Voir les chambres',hero_k='Cuenca · Calle Torres, 1',hero_t='Une pension familiale au centre de Cuenca',hero_s='Une maison historique du XVIe siècle, à deux pas des Maisons suspendues et de la vieille ville.',
 intro_t='Une hospitalité familiale depuis 1966',intro_p1='En septembre 1966, Virgilio Álvarez et Albina Collado ont ouvert l’établissement ; aujourd’hui, l’une de leurs filles le dirige.',
 intro_p2='Le bâtiment, avec un balcon d’angle Renaissance, a été déclaré bien d’intérêt culturel en 1999.',
 stats=['16 chambres','Bien d’intérêt culturel','Restaurant sur place','Wifi gratuit'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Toutes avec salle de bains privée, chauffage central et télévision. Il y a aussi quelques chambres plus petites avec lavabo et salle de bains complète dans le couloir.',
 svcs=['Restaurant de cuisine traditionnelle','Menu du jour','Deux salles pour célébrations','Wifi gratuit','Parking public à 2 minutes à pied','Information sur les allergènes'],
 loc_p='Calle Torres, 1 · 16001 Cuenca. Téléphone : +34 969 211 704. E-mail : info@posadasanjulian.es.',
 chips=['Quelles chambres avez-vous ?','Y a-t-il un petit-déjeuner ?','Où se garer ?','Comment réserver ?']),
'de':dict(title='Posada San Julián · Pension und Restaurant in Cuenca',see_rooms='Zimmer ansehen',hero_k='Cuenca · Calle Torres, 1',hero_t='Eine Familienpension im Zentrum von Cuenca',hero_s='Ein historisches Haus aus dem 16. Jahrhundert, wenige Schritte von den Hängenden Häusern und der Altstadt.',
 intro_t='Familiäre Gastfreundschaft seit 1966',intro_p1='Im September 1966 eröffneten Virgilio Álvarez und Albina Collado das Haus; heute führt es eine ihrer Töchter.',
 intro_p2='Das Gebäude mit seinem Renaissance-Eckbalkon wurde 1999 zum Kulturgut erklärt.',
 stats=['16 Zimmer','Kulturgut','Eigenes Restaurant','Kostenloses WLAN'],nav_rooms='Zimmer',rooms_t='Zimmer',rooms_s='Alle mit eigenem Bad, Zentralheizung und Fernseher. Es gibt auch einige kleinere Zimmer mit Waschbecken und einem vollständigen Bad im Flur.',
 svcs=['Restaurant mit traditioneller Küche','Tagesmenü','Zwei Speisesäle für Feiern','Kostenloses WLAN','Öffentlicher Parkplatz 2 Gehminuten entfernt','Allergeninformationen'],
 loc_p='Calle Torres, 1 · 16001 Cuenca. Telefon: +34 969 211 704. E-Mail: info@posadasanjulian.es.',
 chips=['Welche Zimmer gibt es?','Gibt es Frühstück?','Wo kann ich parken?','Wie kann ich buchen?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement.",
'de':'Diese Seite ist ein Designvorschlag von Berawa, ohne Auftrag der Unterkunft erstellt. Die Texte beruhen auf deren öffentlicher Website; die Bilder sind eigene Illustrationen und zeigen die Unterkunft nicht.'}
BOOK=dict(mode='mail',email='info@posadasanjulian.es')
D=dict(name='Posada San Julián',ac='#2a1d17',ac2='#8a4b2a',ac2_a11y='#7a4124',book=BOOK,around=[],foot=FOOT,
 address='Calle Torres, 1 · 16001 Cuenca',phones=['+34 969 211 704'],emails=['info@posadasanjulian.es'],maps='Posada San Julián, Calle Torres 1, 16001 Cuenca',t=T)
META=dict(repo='demo-hostal-posada-san-julian-cuenca',name='Posada San Julián',legal_name='Eva Álvarez Collado, NIF 04533839X (aviso legal de su web; autónoma)',registry_ids=['04533839X'],
 url='https://www.posadasanjulian.es/',domain='posadasanjulian.es',municipality='Cuenca',province='Cuenca',sector='hostal y restaurante familiar en el centro histórico de Cuenca',
 read_at='2026-11-02T11:04:00+01:00',created_at='2026-11-02T11:04:00+01:00',built_at='2026-11-02T11:20:00+01:00',audit_date='2026-11-02T11:04:00+01:00',
 rating=dict(value=4.2,coincide=['tel','web'],date='2026-10-30',url='https://www.google.com/maps/search/Posada+San+Juli%C3%A1n+Cuenca?hl=es'),
 book=dict(mode='mail',url='mailto:info@posadasanjulian.es',note='sin motor de reservas: su web solo da el teléfono 969 211 704 y el correo info@posadasanjulian.es («Haga su reserva en el teléfono»). Los botones Reservar de la demo abren un correo a info@posadasanjulian.es y el teléfono real va en tel: (mismo criterio que San Martín, Andrín y Hey).'),first_of_type='no aplica: alojamiento con precedente en demos anteriores')
QS={
'es':[('¿Qué habitaciones tenéis?','K01'),('¿Qué tienen las habitaciones?','K02'),('¿Hay desayuno?','K03'),('¿Tenéis restaurante?','K04'),('¿Qué incluye el menú del día?','K05'),('¿Hacéis celebraciones?','K06'),('¿Dónde estáis?','K07'),('¿Cómo reservo?','K08'),('¿Podéis confirmarme disponibilidad para mañana?','K08'),('¿Hay wifi?','K09'),('¿Dónde aparco?','K10'),('¿Cuál es vuestro teléfono?','K11'),('¿Qué puedo ver en Cuenca?','K12'),('¿Cuánto cuesta la noche?',None),('¿Admitís mascotas?',None)],
'en':[('Which rooms do you have?','K01'),('What do the rooms include?','K02'),('Is there breakfast?','K03'),('Do you have a restaurant?','K04'),('What does the set menu include?','K05'),('Do you host celebrations?','K06'),('Where are you?','K07'),('How do I book?','K08'),('Can you confirm availability for tomorrow?','K08'),('Is there wifi?','K09'),('Where can I park?','K10'),('What is your phone number?','K11'),('What can I see in Cuenca?','K12'),('How much is a night?',None),('Do you allow pets?',None)],
'fr':[('Quelles chambres avez-vous ?','K01'),('Que comprennent les chambres ?','K02'),('Y a-t-il un petit-déjeuner ?','K03'),('Avez-vous un restaurant ?','K04'),('Que comprend le menu du jour ?','K05'),('Organisez-vous des célébrations ?','K06'),('Où êtes-vous ?','K07'),('Comment réserver ?','K08'),('Pouvez-vous me confirmer la disponibilité pour demain ?','K08'),('Y a-t-il le wifi ?','K09'),('Où se garer ?','K10'),('Quel est votre numéro de téléphone ?','K11'),('Que voir à Cuenca ?','K12'),('Combien coûte la nuit ?',None),('Acceptez-vous les animaux ?',None)],
'de':[('Welche Zimmer gibt es?','K01'),('Was bieten die Zimmer?','K02'),('Gibt es Frühstück?','K03'),('Haben Sie ein Restaurant?','K04'),('Was beinhaltet das Tagesmenü?','K05'),('Richten Sie Feiern aus?','K06'),('Wo liegt die Pension?','K07'),('Wie kann ich buchen?','K08'),('Können Sie mir die Verfügbarkeit für morgen bestätigen?','K08'),('Gibt es WLAN?','K09'),('Wo kann ich parken?','K10'),('Wie ist Ihre Telefonnummer?','K11'),('Was kann ich in Cuenca sehen?','K12'),('Was kostet eine Nacht?',None),('Sind Haustiere erlaubt?',None)]}
