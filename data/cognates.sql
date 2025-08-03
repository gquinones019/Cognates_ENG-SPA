CREATE DATABASE cognates_db;
ALTER DATABASE cognates_db CHARACTER SET utf8 COLLATE utf8_unicode_ci;
use cognates_db;

CREATE TABLE lexicon (
    id INT NOT NULL AUTO_INCREMENT,
    word VARCHAR(30),
    pos VARCHAR(30),
    definition NVARCHAR(255),
    word_origin NVARCHAR(30),
    lang VARCHAR(30),
    PRIMARY KEY (id)
);

INSERT INTO lexicon
(word, pos, definition, word_origin, lang)

VALUES
    (N'accidental', 'adjective', 'happening by chance; not planned','latin', 'english'),
    (N'accidental', 'adjective', N'casual, contingente', 'latin', 'spanish'),
    (N'anaconda','noun', 'a large South American snake of the boa family, that wraps itself tightly around other animals to kill them before eating them', 'Sinhalese', 'English'),
    (N'anaconda','noun', N'ofidio americano de la misma familia de las boas y de costumbres acuáticas, que pertenece a las especies estranguladoras', 'Sinhalese', 'Spanish'),
    (N'animal', 'noun', 'any living creature, including humans', 'latin', 'English'),
    (N'animal', 'noun', N'ser orgánico que vive, siente y se mueve por propio impulso', 'latin', 'Spanish'),
    (N'banana', 'noun', 'a long curved fruit with a thick yellow skin and that is soft inside, which grows on trees in hot countries','mande', 'English'),
    (N'banana', 'noun', N'fruto comestible del plátano, que es una baya alargada, de diez a quince centímetros de longitud, algo encorvada y de corteza lisa y amarilla', 'mande','spanish'),
    (N'cable', 'noun','a set of wires, covered by plastic, that carries electricity, phone signals, etc.', 'french', 'English'),
    (N'cable', 'noun',N'cordón formado con varios conductores aislados unos de otros y protegido generalmente por una envoltura flexible y resistente', 'french', 'Spanish'),
    (N'cereal', 'noun','a food that is made from grain and eaten with milk, especially in the morning', 'latin', 'English'),
    (N'cereal', 'noun',N'planta gramínea cultivada principalmente por su grano, muy utilizado en la alimentación humana y animal, y de la que existen numerosas especies, como el trigo y la cebada','latin', 'Spanish'),
    (N'coyote','noun','a small wild animal like a dog that lives in North America','nahuatl','english'),
    (N'coyote','noun',N'mamífero carnívoro de Norteamérica, semejante al lobo pero más pequeño y de pelaje gris amarillento','nahuatl', 'spanish'),
    (N'director','noun','a manager of an organization, company, college, etc.','latin','English'),
    (N'director','noun',N'persona que tiene la dirección superior de un cuerpo, de un ramo o de una empresa', 'latin', 'Spanish'),
    (N'flexible', 'adjective', 'able to change or be changed easily according to the situation','latin', 'English'),
    (N'flexible', 'adjective',N'que se adapta con facilidad a la opinión, a la voluntad o a la actitud de otro u otros','latin', 'Spanish'),
    (N'funeral','noun','a (usually religious) ceremony for burying or burning the body of a dead person','latin','English'),
    (N'funeral','noun',N'pompa y solemnidad con que se hace un entierro o unas exequias', 'latin','Spanish'),
    (N'golf','noun','a game played outside on grass in which each player tries to hit a small ball into a series of nine or 18 small holes, using a long, thin stick','english', 'English'),
    (N'golf','noun',N'juego que consiste en recorrer un itinerario fijado dentro de un terreno extenso introduciendo en cada uno de los hoyos practicados en él una bola impelida con palos especiales','English','Spanish'),
    (N'honor', 'noun','a good character, or a reputation for honesty and fair dealing','latin','English'),
    (N'honor', 'noun',N'gloria o buena reputación que sigue a la virtud, al mérito o a las acciones heroicas','latin','Spanish'),
    (N'hospital', 'noun','a place where people who are ill or injured are treated and taken care of by doctors and nurses','latin','English'),
    (N'hospital', 'noun',N'establecimiento destinado al diagnóstico y tratamiento de enfermos, donde a menudo se practican la investigación y la docencia','latin', 'Spanish'),
    (N'hotel','noun','a building where you pay to have a room to sleep in, and where you can sometimes eat meals','french','English'),
    (N'hotel','noun',N'establecimiento de hostelería capaz de alojar con comodidad a huéspedes o viajeros','french','Spanish'),
    (N'idea', 'noun', 'an understanding, thought, or picture in your mind','latin','English'),
    (N'idea', 'noun', N'imagen o representación que del objeto percibido queda en la mente','latin', 'Spanish'),
    (N'incurable','adjective','an understanding, thought, or picture in your mind','latin','English'),
    (N'incurable','adjective',N'imagen o representación que del objeto percibido queda en la mente','latin','Spanish'),
    (N'metal','noun','a chemical element, such as iron or gold, or a mixture of such elements, such as steel, that is generally hard and strong, and through which electricity and heat can travel', 'french','English'),
    (N'metal','noun',N'cada uno de los elementos químicos buenos conductores del calor y de la electricidad, sólidos a temperatura ordinaria, en sus sales en disolución forman iones electropositivos o cationes', 'french','Spanish'),
    (N'natural', 'adjective', 'as found in nature and not involving anything made or done by people','latin','English'),
    (N'natural', 'adjective', N'perteneciente o relativo a la naturaleza o conforme a la cualidad o propiedad de las cosas','latin', 'Spanish'),
    (N'piano', 'noun','a large musical instrument with a row of black and white keys that are pressed to play notes','italian', 'English'),
    (N'piano', 'noun',N'instrumento musical de cuerdas generalmente metálicas dispuestas dentro de una caja de resonancia, que son golpeadas por macillos accionados desde un teclado','Spanish', 'Spanish'),
    (N'television','noun','a device shaped like a box with a screen that receives electrical signals and changes them into moving images and sound, or the method or business of sending images and sound by electrical signals','english','English'),
    (N'television','noun',N'sistema de transmisión de imágenes a distancia a través de diferentes medios electromagnéticos, y que se reproducen posteriormente en un aparato receptor','english','Spanish'),
    (N'terrible','adjective','used to emphasize the great degree of something','latin', 'English'),
    (N'terrible','adjective',N'muy grande o desmesurado','latin','Spanish'),
    (N'triple', 'adjective','having three parts of the same type, or happening three times','latin','English'),
    (N'triple', 'adjective',N'tres veces mayor o que contiene una cantidad tres veces exactamente','latin','Spanish'),
    (N'vegetables', 'noun', 'a plant that is used as food, or the part of a plant, such as a root, stem, or flower, that is used as food', 'latin','English'),
    (N'vegetables', 'noun', N'planta comestible que se cultiva en las huertas.', 'latin','English')
;