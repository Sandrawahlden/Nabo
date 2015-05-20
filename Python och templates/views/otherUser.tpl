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
				<p id="user">
				<a href="/myProfile/">{{username}}   </a>
				<a href="/">  Logga ut</a>
				</p>
			</div>
		</header>

		<nav>
			<nav class="profile">
				<ul>
					<li><a href="/myProfile/" clas="nav"> Min Profil </a></li>
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
				<img src="{{prof_pic}}" alt="Bild på {{first}}" id="profilePic" style="width:150px;height:150px;padding:10px">
				
				<p id="name"><span style="font-weight:bold"> {{first}} {{last}}</span></p>
				<p id="age"><span style="font-weight:bold"> {{age_2}} år</span></p>
				<p id="apartment"><span style="font-weight:bold">Våning:</span> {{apa}}</p>
				<p id="phone"><span style="font-weight:bold">Telefon:</span> {{tele}}</p>
					
				<p id="likes"><span style="font-weight:bold">Om </span>{{first}}: <br>
				{{likees}}</p>	
		</div>
		

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>