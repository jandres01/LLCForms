Form **SS-4 Application for Employer Identification Number**

1.What is the legal name of the entity (or individual) for whom the EIN is being requested? (previously submitted)
[BR]
${entity.name}

2.What is the trade name of your business(if different from line 1)?

3.What is the name of the Executor, administrator, trustee, "care of"?

4a. What is the mailing address? 
[BR]
${entity.address.address}

4b. What is the city, state and Zip code of the business?
[BR]
${entity.address.city} ${entity.address.state} ${entity.address.zip}

5a. What is the street address(if different from question 4) ?
[BR]
% if entity.mail is True:
  ${entity.address}
% else:
  ${organizer.address}
% endif

5b. What is the city, state and Zip code(if different?)
[BR]
${entity.address.city} ${entity.address.state} ${entity.address.zip}

6.What is the county and state where the principal business is located?
[BR]
${entity.address.county} ${entity.address.state}

7a. What is the name of the responsible party?
[BR]
${entity.name} 

7b. What is the responsible party’s SSN, ITIN or EIN?

8a. Is this application for a limited liability company(LLC)? Yes

8b. If 8a is “Yes,”(yes) how many LLC members?

8c. If 8a is “Yes,” (yes) was the LLC organized in the United States?  (yes)

9a. What is the **Type of entity**(check only one box)? **Caution** If 8a is “Yes,” see the      instructions for the correct box to check

9b. If a corporation, what is the name of the state or foreign county (if applicable) where incorporated?

10.What is your **Reason for applying**?

11.What was the date the business started or acquired (month, day, year)?

12.What is the closing month of the accounting year?

13.What is the highest number of employees expected in the next 12 months?

14.If you expect your employment tax liability to be $1,000 or less in a full calendar year **and** want to file Form 941 quarterly, check here. (Your employment tax liability generally will be $1,000 or less if you expect to pay $4,000 or less in total wages.) If you do not check this box, you must file Form 941 for every quarter.

15.What was the first date the wages or annuities were paid(month, day, year)? **Note.** If applicant is withholding agent, enter date income will first be paid to nonresident alien (month, day, year).

16.What is the principal activity of your business? (check **one** box)

17.What is the principal line of merchandise sold, specific construction work done, products produced, or services provided?

18.Has the applicant entity shown on line 1 ever applied for an EIN? If “Yes,” write previous EIN here. 

**Third Party Designee**

What is the Designee’s name?

What is the Designee’s Address and ZIP code?

What is the Designee’s telephone number (include area code)?

What is the Designee’s fax number (include area code)?

What is the Applicant’s telephone number (include area code)?

What is the Applicant’s fax number (include area code)? 

Under penalties of perjury, I declare that I have examined this application, and to the best of my knowledge and belief, it is true, correct and complete. What is the name and title?

What is the date of signing?


