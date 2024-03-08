User:
- id INT PRIMARY KEY
- name VARCHAR(255)
- email VARCHAR(255) UNIQUE
- encryptedPassword VARCHAR(255)

Portfolio:
- id INT PRIMARY KEY
- userId INT FOREIGN KEY REFERENCES User(id)
- name VARCHAR(255)
- description TEXT

Asset:
- id INT PRIMARY KEY
- name VARCHAR(255)
- type VARCHAR(50)
- ticker VARCHAR(10)

PortfolioAssetDetails:
- portfolioId INT FOREIGN KEY REFERENCES Portfolio(id)
- assetId INT FOREIGN KEY REFERENCES Asset(id)
- quantity DECIMAL(18,4)
- averageAcquisitionValue DECIMAL(18,4)
- currentValue DECIMAL(18,4)
- profitability DECIMAL(18,4)

Transaction:
- id INT PRIMARY KEY
- portfolioId INT FOREIGN KEY REFERENCES Portfolio(id)
- assetId INT FOREIGN KEY REFERENCES Asset(id)
- type ENUM('buy', 'sell')
- quantity DECIMAL(18,4)
- price DECIMAL(18,4)
- transactionDate DATETIME

AssetPriceHistory:
- id INT PRIMARY KEY
- assetId INT FOREIGN KEY REFERENCES Asset(id)
- dateTime DATETIME
- closingPrice DECIMAL(18,4)
- openingPrice DECIMAL(18,4)
- high DECIMAL(18,4)
- low DECIMAL(18,4)
- volume DECIMAL(18,4)

AssetProjection:
- id INT PRIMARY KEY
- assetId INT FOREIGN KEY REFERENCES Asset(id)
- projectionDate DATETIME
- projectedPrice DECIMAL(18,4)
- projectionMethod VARCHAR(255)

PriceAlert:
- id INT PRIMARY KEY
- userId INT FOREIGN KEY REFERENCES User(id)
- assetId INT FOREIGN KEY REFERENCES Asset(id)
- triggerPrice DECIMAL(18,4)
- alertType ENUM('above', 'below')
- isActive BOOLEAN

UserPreferences:
- id INT PRIMARY KEY
- userId INT FOREIGN KEY REFERENCES User(id)
- visualizationSettings TEXT
- notificationSettings TEXT

ActivityLog:
- id INT PRIMARY KEY
- userId INT FOREIGN KEY REFERENCES User(id)
- activityDescription TEXT
- dateTime DATETIME
