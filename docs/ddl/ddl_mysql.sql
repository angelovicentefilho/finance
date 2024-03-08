CREATE TABLE user (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    encrypted_password VARCHAR(255) NOT NULL
);

CREATE TABLE portfolio (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    name VARCHAR(255) NOT NULL,
    description TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE asset (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    type VARCHAR(50) NOT NULL,
    ticker VARCHAR(10) NOT NULL
);

CREATE TABLE portfolio_asset_details (
    portfolio_id INT NOT NULL,
    asset_id INT NOT NULL,
    quantity DECIMAL(18,4) NOT NULL,
    average_acquisition_value DECIMAL(18,4) NOT NULL,
    current_value DECIMAL(18,4) NOT NULL,
    profitability DECIMAL(18,4) NOT NULL,
    PRIMARY KEY (portfolio_id, asset_id),
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
    FOREIGN KEY (asset_id) REFERENCES asset(id)
);

CREATE TABLE transaction (
    id INT AUTO_INCREMENT PRIMARY KEY,
    portfolio_id INT NOT NULL,
    asset_id INT NOT NULL,
    type ENUM('buy', 'sell') NOT NULL,
    quantity DECIMAL(18,4) NOT NULL,
    price DECIMAL(18,4) NOT NULL,
    transaction_date DATETIME NOT NULL,
    FOREIGN KEY (portfolio_id) REFERENCES portfolio(id),
    FOREIGN KEY (asset_id) REFERENCES asset(id)
);

CREATE TABLE asset_price_history (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT NOT NULL,
    date_time DATETIME NOT NULL,
    closing_price DECIMAL(18,4) NOT NULL,
    opening_price DECIMAL(18,4) NOT NULL,
    high DECIMAL(18,4) NOT NULL,
    low DECIMAL(18,4) NOT NULL,
    volume DECIMAL(18,4) NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES asset(id)
);

CREATE TABLE asset_projection (
    id INT AUTO_INCREMENT PRIMARY KEY,
    asset_id INT NOT NULL,
    projection_date DATETIME NOT NULL,
    projected_drice DECIMAL(18,4) NOT NULL,
    projection_method VARCHAR(255) NOT NULL,
    FOREIGN KEY (asset_id) REFERENCES asset(id)
);

CREATE TABLE price_alert (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    asset_id INT NOT NULL,
    trigger_price DECIMAL(18,4) NOT NULL,
    alert_type ENUM('above', 'below') NOT NULL,
    active BOOLEAN NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (asset_id) REFERENCES asset(id)
);

CREATE TABLE user_preferences (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    visualization_settings TEXT,
    notification_settings TEXT,
    FOREIGN KEY (user_id) REFERENCES user(id)
);

CREATE TABLE activity_log (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    activity_description TEXT NOT NULL,
    date_time DATETIME NOT NULL,
    FOREIGN KEY (user_id) REFERENCES user(id)
);
