<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>


	<div id="wrapper">

		<header>
			<div id="logga">
				<a href="/home/">
				<img src="/static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0"></a>
			</div>
			<div id="loggaUt">
				<p id="adress"> Rönnblomsgatan 11</p>
				<p class="user">
				<a href="/myProfile/">{{username}}</a>
				<a href="/">Logga ut</a>
			</p>
			</div>
		</header>

		<nav>
			<nav class="profile">
				<ul>
					<li><a href="/myProfile/" class="nav"> Min Profil </a></li>
					<li><a href="/editProfile/" class="nav">Redigera min profil</a></li>
				</ul>
			</nav>

			<nav class="board">
				<ul>
					<li><a href="/home/" class="nav">Anslagstavlan</a></li>
				</ul>
			</nav>

			<nav class="messagesClick">
				<ul>
					<li><a href="/inbox/" class="nav">Mina meddelanden</a></li>
					<li><a href="/write/" class="nav"><span style="color: #4d6630">Skriv nytt meddelande</span></a></li>
				</ul>
			</nav>

			<nav class="nabos">
				<ul>
					<li><a href="/nabos/" class="nav">Nabos</a></li>
				</ul>
			</nav>
		</nav>

		<div id="content">
			<div id="ListOfNabos">
			%for name, pic, user in zip(name_list, pic_list, user_list):
				<div id="naboRutaWrite">
					<img src="{{pic}}" alt="{{name}}" style="width:50px;height:50px;padding:5px">
					<a href="/otherUser/{{user}}">{{name}}</a>
					<br>
					<br>
				</div>
			%end
			</div>
				
		<div id="sendFields">
				<p id="writeANewMessage">Till
				</p>

				<p id="writeYourMessageHere">Meddelande
				</p>

				<p id="sendYourMessageButton">Skicka!
				</p>
			
		</div>
	</div>
		
		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>


	</div>
</html>