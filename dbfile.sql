CREATE TABLE users (
uid INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
firstname VARCHAR(100) NOT NULL,
lastname VARCHAR(100) NOT NULL,
email VARCHAR(120) NOT NULL UNIQUE,
pwdhash VARCHAR(100) NOT NULL
);

CREATE TABLE campaigner
(
credits INT,
email VARCHAR(120) NOT NULL,
datecreated DATETIME NOT NULL DEFAULT NOW()
);

CREATE TABLE subscriber
(
    sid INT PRIMARY KEY AUTO_INCREMENT,
    sname VARCHAR(50) NOT NULL ,
    semailid VARCHAR(120) NOT NULL UNIQUE,
    stime DATETIME NOT NULL DEFAULT NOW()
);


CREATE TABLE category
(
    cid INT PRIMARY KEY AUTO_INCREMENT,
    cname VARCHAR(50) NOT NULL UNIQUE,
    ctime DATETIME NOT NULL DEFAULT NOW()
);


CREATE TABLE category_subscriber
(
    csid INT AUTO_INCREMENT PRIMARY KEY,
    catname VARCHAR(120) NOT NULL,
    subname VARCHAR(120) NOT NULL,
    submailid VARCHAR(120) NOT NULL,
    cscampaignermailid VARCHAR(120) NOT NULL,
    cstime DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (cscampaignermailid) REFERENCES campaigner(email),
    CONSTRAINT check_cons UNIQUE(cscampaignermailid, catname, subname, submailid )
);

CREATE TABLE unsubscribers
(
    usid INT AUTO_INCREMENT PRIMARY KEY,
    usname VARCHAR(120) NOT NULL,
    usmailid VARCHAR(120) NOT NULL,
    CONSTRAINT check_cons UNIQUE (usname, usmailid ),
    untime DATETIME NOT NULL DEFAULT NOW()
);

CREATE TABLE campaign
(
    cpid INT AUTO_INCREMENT PRIMARY KEY,
    cpcampaignermailid VARCHAR(120) NOT NULL,
    cpsubject VARCHAR(120) NOT NULL,
    cpcategory VARCHAR(120) NOT NULL,
    cpcontent VARCHAR(65000) NOT NULL,
    cptime DATETIME NOT NULL DEFAULT NOW(),
    FOREIGN KEY (cpcategory) REFERENCES category(cname), 
    FOREIGN KEY (cpcampaignermailid) REFERENCES campaigner(email),    
    CONSTRAINT check_cons UNIQUE(cpcampaignermailid, cpsubject)
);
