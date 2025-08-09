CREATE DATABASE cognates_db;
ALTER DATABASE cognates_db CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use cognates_db;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(30),
    pos VARCHAR(30),
    definition VARCHAR(255),
    word_origin VARCHAR(30),
    lang VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO lexicon
(word, pos, definition, word_origin, lang)

VALUES
    ('accidental', 'adjective', 'happening by chance; not planned', 'latin', 'English'),
    ('accidental', 'adjective', 'casual, contingente', 'latin', 'Spanish'),
    ('anaconda','noun', 'a large South American snake of the boa family, that wraps itself tightly around other animals to kill them before eating them', 'sinhalese', 'English'),
    ('anaconda','noun', 'ofidio americano de la misma familia de las boas y de costumbres acuáticas, que pertenece a las especies estranguladoras', 'sinhalese', 'Spanish'),
    ('animal', 'noun', 'any living creature, including humans', 'latin', 'English'),
    ('animal', 'noun', 'ser orgánico que vive, siente y se mueve por propio impulso', 'latin', 'Spanish'),
    ('banana', 'noun', 'a long curved fruit with a thick yellow skin and that is soft inside, which grows on trees in hot countries','mande', 'English'),
    ('banana', 'noun', 'fruto comestible del plátano, que es una baya alargada, de diez a quince centímetros de longitud, algo encorvada y de corteza lisa y amarilla', 'mande','Spanish'),
    ('cable', 'noun','a set of wires, covered by plastic, that carries electricity, phone signals, etc.', 'french', 'English'),
    ('cable', 'noun','cordón formado con varios conductores aislados unos de otros y protegido generalmente por una envoltura flexible y resistente', 'french', 'Spanish'),
    ('cereal', 'noun','a food that is made from grain and eaten with milk, especially in the morning', 'latin', 'English'),
    ('cereal', 'noun','planta gramínea cultivada principalmente por su grano, muy utilizado en la alimentación humana y animal, y de la que existen numerosas especies, como el trigo y la cebada','latin', 'Spanish'),
    ('coyote','noun','a small wild animal like a dog that lives in North America','nahuatl','English'),
    ('coyote','noun','mamífero carnívoro de Norteamérica, semejante al lobo pero más pequeño y de pelaje gris amarillento','nahuatl', 'Spanish'),
    ('director','noun','a manager of an organization, company, college, etc.','latin','English'),
    ('director','noun','persona que tiene la dirección superior de un cuerpo, de un ramo o de una empresa', 'latin', 'Spanish'),
    ('flexible', 'adjective', 'able to change or be changed easily according to the situation','latin', 'English'),
    ('flexible', 'adjective','que se adapta con facilidad a la opinión, a la voluntad o a la actitud de otro u otros','latin', 'Spanish'),
    ('funeral','noun','a (usually religious) ceremony for burying or burning the body of a dead person','latin','English'),
    ('funeral','noun','pompa y solemnidad con que se hace un entierro o unas exequias', 'latin','Spanish'),
    ('golf','noun','a game played outside on grass in which each player tries to hit a small ball into a series of nine or 18 small holes, using a long, thin stick','english', 'English'),
    ('golf','noun','juego que consiste en recorrer un itinerario fijado dentro de un terreno extenso introduciendo en cada uno de los hoyos practicados en él una bola impelida con palos especiales','english','Spanish'),
    ('honor', 'noun','a good character, or a reputation for honesty and fair dealing','latin','English'),
    ('honor', 'noun','gloria o buena reputación que sigue a la virtud, al mérito o a las acciones heroicas','latin','Spanish'),
    ('hospital', 'noun','a place where people who are ill or injured are treated and taken care of by doctors and nurses','latin','English'),
    ('hospital', 'noun','establecimiento destinado al diagnóstico y tratamiento de enfermos, donde a menudo se practican la investigación y la docencia','latin', 'Spanish'),
    ('hotel','noun','a building where you pay to have a room to sleep in, and where you can sometimes eat meals','french','English'),
    ('hotel','noun','establecimiento de hostelería capaz de alojar con comodidad a huéspedes o viajeros','french','Spanish'),
    ('idea', 'noun', 'an understanding, thought, or picture in your mind','latin','English'),
    ('idea', 'noun', 'imagen o representación que del objeto percibido queda en la mente','latin', 'Spanish'),
    ('incurable','adjective','an understanding, thought, or picture in your mind','latin','English'),
    ('incurable','adjective','imagen o representación que del objeto percibido queda en la mente','latin','Spanish'),
    ('metal','noun','a chemical element, such as iron or gold, or a mixture of such elements, such as steel, that is generally hard and strong, and through which electricity and heat can travel', 'french','English'),
    ('metal','noun','cada uno de los elementos químicos buenos conductores del calor y de la electricidad, sólidos a temperatura ordinaria, en sus sales en disolución forman iones electropositivos o cationes', 'french','Spanish'),
    ('natural', 'adjective', 'as found in nature and not involving anything made or done by people','latin','English'),
    ('natural', 'adjective', 'perteneciente o relativo a la naturaleza o conforme a la cualidad o propiedad de las cosas','latin', 'Spanish'),
    ('piano', 'noun','a large musical instrument with a row of black and white keys that are pressed to play notes','italian', 'English'),
    ('piano', 'noun','instrumento musical de cuerdas generalmente metálicas dispuestas dentro de una caja de resonancia, que son golpeadas por macillos accionados desde un teclado','italian', 'Spanish'),
    ('television','noun','a device shaped like a box with a screen that receives electrical signals and changes them into moving images and sound, or the method or business of sending images and sound by electrical signals','english','English'),
    ('television','noun','sistema de transmisión de imágenes a distancia a través de diferentes medios electromagnéticos, y que se reproducen posteriormente en un aparato receptor','english','Spanish'),
    ('terrible','adjective','used to emphasize the great degree of something','latin', 'English'),
    ('terrible','adjective','muy grande o desmesurado','latin','Spanish'),
    ('triple', 'adjective','having three parts of the same type, or happening three times','latin','English'),
    ('triple', 'adjective','tres veces mayor o que contiene una cantidad tres veces exactamente','latin','Spanish'),
    ('vegetables', 'noun', 'a plant that is used as food, or the part of a plant, such as a root, stem, or flower, that is used as food', 'latin','English'),
    ('vegetables', 'noun', 'planta comestible que se cultiva en las huertas.', 'latin','Spanish')
;


CREATE TABLE false_friends (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(30),
    pos VARCHAR(30),
    definition VARCHAR(255),
    word_origin VARCHAR(30),
    lang VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO false_friends
(word, pos, definition, word_origin, lang)

VALUES
    ('conductor','noun', 'Someone who directs the performance of musicians or a piece of music.', 'latin', 'English' ),
    ('conductor','adjective', 'Que conduce.', 'latin', 'Spanish'),
    ('diversion', 'noun', 'Act of turning aside from a course of action.', 'latin', 'English'),
    ('diversión', 'noun', 'Entretenimiento, distracción, alegría.', 'latin', 'Spanish'),
    ('familiar', 'adjective', 'Easy to recognize because of being seen, met, heard, etc. before.', 'latin', 'English'),
    ('familiar', 'adjective', 'Perteneciente o relativo a la familia.', 'latin', 'Spanish'),
    ('hay', 'noun','Grass that is cut and dried and used as animal food.', 'proto germanic', 'English'),
    ('hay', 'verb','Forma impersonal del verbo "haber" y se usa para indicar la existencia de algo.', 'latin', 'Spanish'),
    ('mayor', 'noun', 'The elected leader of a city or town.','latin', 'English'),
    ('mayor', 'adjective', 'Superior, grande.','latin', 'Spanish'),
    ('once', 'adjective', 'One single time in the past, but not now.', 'proto indo european', 'English'),
    ('once', 'noun', 'Número natural que sigue al diez.', 'latin', 'Spanish'),
    ('pan', 'noun', 'A metal container that is round and often has a long handle and a lid, used for cooking things on top of a cooker.', 'proto germanic', 'English'),
    ('pan', 'noun', 'Alimento que consiste en una masa de harina, por lo común de trigo, levadura y agua, cocida en un horno.', 'latin', 'Spanish'),
    ('pie', 'noun', 'A type of food made with meat, vegetables, or fruit covered in pastry and baked.', 'latin', 'English'),
    ('pie', 'noun', 'Extremidad de cada uno de los dos miembros inferiores del cuerpo humano.', 'latin', 'Spanish'),
    ('red','adjective','Of the color of fresh blood', 'proto german', 'English'),
    ('red','noun','Extremidad de cada uno de los dos miembros inferiores del cuerpo humano.', 'latin', 'Spanish'),
    ('sin', 'noun', 'The offence of breaking, or the breaking of, a religious or moral law.', 'proto germanic', 'English'),
    ('sin', 'preposition', 'Denota carencia o falta de algo.', 'latin', 'Spanish')
;