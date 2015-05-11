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
				<p id="user">
				<a href="/myProfile/">{{username}}</a>
				<a href="/">Logga ut</a>
			</div>
		</header>

		<nav>
			<nav id="profile">
				<ul>
					<li><p id="user"><a href="/myProfile/">{{username}}</a></p></li>
					<li><a href="/editProfile/" class="nav">Redigera min profil</a></li>
				</ul>
			</nav>

			<nav id="board">
				<ul>
					<li><a href="/home/" class="nav">Anslagstavlan</a></li>
				</ul>
			</nav>

			<nav id="messages">
				<ul>
					<li><a href="/inbox/" class="nav">Mina meddelanden</a></li>
					<li><a href="/write/" class="nav">Skriv nytt meddelande</a></li>
				</ul>
			</nav>

			<nav id="nabos">
				<ul>
					<li><a href="/nabos/" class="nav">Nabos</a></li>
				</ul>
			</nav>
		</nav>

		<div id="content"
			<div id="bodySquare">
				<p>Här kommer vi fylla på med innehåll.
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