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
				<a href="/myProfile/">{{username}}   </a>
				<a href="/">  Logga ut</a>
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

			<nav class="messages">
				<ul>
					<li><a href="/inbox/" class="nav">Mina meddelanden</a></li>
					<li><a href="/write/" class="nav">Skriv nytt meddelande</a></li>
				</ul>
			</nav>

			<nav class="nabosClick">
				<ul>
					<li><a href="/nabos/" class="nav"><span style="color: #4d6630">Nabos</span></a></li>
				</ul>
			</nav>
		</nav>

		<div id="content">
			%for name, pic, user in zip(name_list, pic_list, user_list):
				<div id="naboRuta">
					<img src="{{pic}}" alt="{{name}}" style="width:60px;height:60px;padding:5px" id="naboListPic">
					<a href="/otherUser/{{user}}" id="naboListName">{{name}}</a>
					<a href="/write/"><img src="/static/Bilder/Envelope.png" alt="Skicka meddelande" style="width:20px;height:20px;padding:5px" id="naboListEnvelope"></a>
				</div>
			%end
		</div>
		
		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>
	
	</div>
</html>