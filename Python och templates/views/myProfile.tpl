<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>{{username}}</title>
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
				<p id="adress">Rönnblommsgatan 11</p>
				<p id="user">
				<a href="/myProfile/">{{username}}</a>
				<a href="/">Logga ut</a>
			</div>
		</header>

		<nav>
			<nav class="profileClick">
				<ul>
					<li><p id="user"><a href="/myProfile/">{{username}}</a></p></li>
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

			<nav class="nabos">
				<ul>
					<li><a href="/nabos/" class="nav">Nabos</a></li>
				</ul>
			</nav>
		</nav>

		<div id="content">
			<div id="bodySquare">
				<img src="{{profile_pic}}" alt="Bild på dig" id="profilePic" style="width:150px;height:150px;padding:10px">
				
				<p id="name"><span style="font-weight:bold">Namn:</span> {{username}}</p>
				<p id="age"><span style="font-weight:bold">Ålder:</span> {{age_1}}</p>
				<p id="apartment"><span style="font-weight:bold">Våning:</span> {{appartment}}</p>
				<p id="phone"><span style="font-weight:bold">Telefonnr:</span> {{tel}}</p>
					
				<p id="likes"><span style="font-weight:bold">Om {{firstname}}:</span> <br>
				{{like}}</p>
				
			</div>

			<div id="clickToEditProfile">
				<a href="/editProfile/">Redigera min profil</a>
			</div>
		</div>

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>