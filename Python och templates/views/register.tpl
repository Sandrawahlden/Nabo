<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="/static/style.css">
		<script type="text/javascript" src=""/static/JS/Password check.js""></script>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	
	<div id="indexWrapper">
		<header>
			<div id="logga">
				<a href="/">
					<img src="/static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0">
				</a>
			</div>
		</header>
	</header>

	<body>
		

		<div id="welcomeText">
			<h1>Välkommen NAMN!</h1>
			<p id="welcomeTextFirstPage">Nu återstår att registrera din adress så att vi kan koppla ihop dig med dina grannar</p>
		</div>
		

		<div id="signUp">
			<p id="indexPageText">SKAPA ANVÄNDARE</p>	
			
			<form action="/myProfile/" method="POST" class="form">
				
				<p class="adress">
					<input required type="text" name="adress" id="adress" placeholder="Gatuadress">	
				</p>

				<p class="adress">
					<input required type="text" name="adress" id="city" placeholder="Postort">	
				</p>

				
					
				<p class="submit">
					<input name="register" id="button1" type="submit" value="Registrera">
				</p>
			</form>
		</div>


	</body>
</html>


