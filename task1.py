str="Before departure, all students leaving for exchange studies should fill in a specialized application form. An application should be submitted in I copy and not later than 2 weeks prior to departure for the exchange semester; provided that the students do not have any academic failure. The paper should be submitted to the International Academic Mobility Office (Volkhovsky per:, 3, office 207, Tel.: +7 (812) 323 8447). A copy of the invitation letter from a host school - partner of GSOM SPbU has to be attached to the application."

n1=str.index("(")
n2=str.index(", Tel.")

address=str[n1+1:n2]
address
#as for me, everything is good. Try "print(address)" if you wand. We need smth for PR hahaha
