library(lubridate)
library(ggplot2)

# Create a data frame
activity_data <- data.frame(
  Date = as.Date(c("2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05")),
  Count = c(10, 12, 15, 8, 20)
)

# Add weekday and week of year columns
activity_data$Weekday <- factor(wday(activity_data$Date, label = TRUE, week_start = 1), 
                                levels = c("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"))
activity_data$Week <- week(activity_data$Date)

# Plot calendar heatmap
ggplot(activity_data, aes(x = Weekday, y = Week, fill = Count)) +
  geom_tile(color = "white") +
  scale_fill_gradient(low = "white", high = "blue") +
  labs(title = "Daily Activity Count",
       x = "Weekday",
       y = "Week",
       fill = "Count") +
  theme_minimal()
