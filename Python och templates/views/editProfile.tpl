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
				<div id="editProfile">
					<p>Redigera Profil</p>	
						<form action="/myProfile/" method="POST" class="form">
						
						<p class ="profile_pic">
							<input required type="text" name="profile_pic" id="profile_pic" placeholder="URL till önskad bild:">	
						</p>
						
						<p class ="name">
							<input required type="text" name="name" id="name" placeholder="Förnamn:">	
						</p>
							
						<p class="surname">
							<input required type="text" name="surname" id="surname" placeholder="Efternamn:">	
						</p>
						
						<p class="adress">
							<input required type="text" name="street" id="street" placeholder="Gata och gatnummer:">	
						</p>
						
						<p class="adress">
							<input required type="text" name="city" id="city" placeholder="Stad:">	
						</p>
						
						<p class="email">
							<input required type="email" name="email" id="email" placeholder="Email:">			
						</p>
						<p>Byta lösenord</p>
						<p class="password">
							<input type="password" required name="old_pwd" id="password" placeholder="Gammalt lösenord:">	
						</p>
						<p class="password">
							<input type="password" required name="pwd_1" id="password" placeholder="Nytt lösenord:">	
						</p>

						<p class="password">
							<input type="password" required name="pwd_2" id="password" placeholder="Bekräfta nytt lösenord:">	
						</p>
						
						<p class="submit">
							<input name="update" type="submit" value="Uppdatera">
						</p>
				</form>
			</div>
		</div>
		

		<footer>
			<a href="/contact/">Kontakta oss</a>
			<a href="/about/">Om Nabo</a>
			<a href="/help/">Hjälp</a>
		</footer>

	</div>
</html>