# Step 1: Install ggplot2 if not already installed
if (!require(ggplot2)) {
  install.packages("ggplot2")
}

# Step 2: Load ggplot2
library(ggplot2)

# Verify if ggplot2 is loaded successfully
if ("ggplot2" %in% .packages()) {
  print("ggplot2 is loaded successfully")
} else {
  print("ggplot2 is not loaded")
}

# Step 3: Create data frame and plot
revenue_data <- data.frame(
  Year = 2015:2019,
  Revenue = c(30, 35, 40, 45, 50)
)

# Plot area plot
ggplot(revenue_data, aes(x = Year, y = Revenue)) +
  geom_area(fill = "skyblue", alpha = 0.5) +
  labs(title = "Yearly Revenue",
       x = "Year",
       y = "Revenue (in million)") +
  theme_minimal()
