<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>nabo</title>
		<link rel="stylesheet" href="../static/style.css">
		<script type="text/javascript" src=""/static/JS/Password check.js""></script>
		<meta name="viewport" content="width=device-width, initial-scale=1.0">
	</head>
	
	<div id="indexWrapper">
		<header>
			<div id="logga">
				<a href="/">
<<<<<<< HEAD
<<<<<<< HEAD
					<img src="/static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0" >
=======
					<img src="/static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0">
>>>>>>> 104b04ece1a7101ab746d99cfee46c89a2957fa4
=======
					<img src="../static/Bilder/logotypnabo.jpg" alt="Nabologga" style="width:260px;height:82px;border:0">
>>>>>>> 308d4b52d4189cfa624d230c4ed66e0b9c873739
				</a>
			</div>
		</header>
	</header>

	<body>

	<div id="mamaWrapper">
		<div id="signin">
				<p id="indexPageText">LOGGA IN</p>

				<form action="/home/" method="POST" class="form">
				
					<p>
						<input required type="email" name="mail" id="email" placeholder="Email">s
					</p>			
					
					<p>
						<input required type="password" name="pwd" id="password" placeholder="Lösenord">	
					</p>
			
					<p class="submit">
						<input name="sign_in" type="submit" value="Logga in">
					</p>
				</form>
		</div>

		<div id="welcomeText">
			<h1>Välkommen till Nabo!</h1>
			<p id="welcomeTextFirstPage">Nabo hjälper dig att identifiera och interagera med grannarna i din trappuppgång. Låna en hammare, skaffa kattvakt eller bjud in till gårdsfest. </p>
	</div>
		
	<div id="secondIndexWrapper">
		<div id="signUp">
			<p id="indexPageText">SKAPA ANVÄNDARE</p>	
				<form action="/myProfile/" method="POST" class="form">
				
					<p class ="name">
						<input required type="text" name="name" id="name" placeholder="Förnamn">	
					
						<input required type="text" name="surname" id="surname" placeholder="Efternamn">	
					</p>
					
					<p class="email">
						<input required type="email" name="email" id="emailLI" placeholder="Email">			
					</p>

					<p class="password">
						<input type="password" required name="pwd_1" id="passwordLI" placeholder="Lösenord">	
					
						<input type="password" required name="pwd_2" id="passwordLI" placeholder="Bekräfta lösenord">	
					</p>

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
	</div>
</div>
		


	</body>
</html>


