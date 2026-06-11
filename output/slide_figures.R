# Slide-deck scatter figures (slides 3-6) \u2014 ggplot2 + ggrepel + ragg.
# Renders output/slide{3_quadrant,4_children,5_wra,6_population}.png
suppressMessages({library(ggplot2); library(ggrepel); library(ragg)})
FONT <- "Helvetica Neue"
update_geom_defaults("text", list(family = FONT))

tx <- 5.5; ty <- 5.5
ARR <- "\u2192"; EMD <- "\u2014"   # arrow, em-dash (ASCII-safe escapes)
tier_cols   <- c(T1 = "#1e7a3c", T2 = "#2e5c8a", T3 = "#c0392b")
tier_labels <- c(T1 = paste("Tier 1", EMD, "strong + cost-effective"),
                 T2 = paste("Tier 2", EMD, "strong / mixed"),
                 T3 = paste("Tier 3", EMD, "promising / indirect"))

# df: label,x,y,tier | xlabs/ylabs: 2-elem axis tick labels | annos: corner labels (x,y,label,hjust,vjust,color)
quad_plot <- function(df, xlab, ylab, xlabs, ylabs, annos, outfile, w = 7.2, h = 5.3) {
  df$tier <- droplevels(factor(df$tier, levels = c("T1","T2","T3")))
  pres <- levels(df$tier)
  p <- ggplot(df, aes(x, y)) +
    annotate("rect", xmin = tx, xmax = 10, ymin = ty, ymax = 10, fill = "#e8f8e8", alpha = 0.6) +
    annotate("rect", xmin = 1,  xmax = tx, ymin = ty, ymax = 10, fill = "#e8f4fd", alpha = 0.6) +
    annotate("rect", xmin = 1,  xmax = tx, ymin = 1,  ymax = ty, fill = "#fde8e8", alpha = 0.6) +
    annotate("rect", xmin = tx, xmax = 10, ymin = 1,  ymax = ty, fill = "#fdf8e8", alpha = 0.6) +
    geom_vline(xintercept = tx, linetype = "22", color = "#1b365d", alpha = 0.4) +
    geom_hline(yintercept = ty, linetype = "22", color = "#1b365d", alpha = 0.4)
  for (i in seq_len(nrow(annos))) {
    a <- annos[i, ]
    p <- p + annotate("text", x = a$x, y = a$y, label = a$label, hjust = a$hjust,
                      vjust = a$vjust, color = a$color, fontface = "bold", size = 2.85)
  }
  p <- p +
    geom_point(aes(color = tier), size = 3.7, alpha = 0.9) +
    geom_text_repel(aes(label = label), size = 3.0, color = "#1a1a2e", family = FONT,
                    box.padding = 0.5, point.padding = 0.3, min.segment.length = 0,
                    segment.color = "#9aa7b4", segment.size = 0.3, max.overlaps = Inf,
                    force = 2, seed = 7) +
    scale_color_manual(values = tier_cols[pres], labels = tier_labels[pres], name = NULL) +
    scale_x_continuous(limits = c(1, 10), breaks = c(2, 9), labels = xlabs, expand = c(0, 0)) +
    scale_y_continuous(limits = c(1, 10), breaks = c(2, 9), labels = ylabs, expand = c(0, 0)) +
    labs(x = paste(xlab, ARR), y = paste(ylab, ARR)) +
    theme_minimal(base_size = 12, base_family = FONT) +
    theme(legend.position = "top", legend.justification = "left",
          legend.text = element_text(size = 9, color = "#1a1a2e"), legend.margin = margin(0,0,2,0),
          panel.grid = element_blank(),
          axis.title.x = element_text(color = "#1b365d", face = "bold", size = 10.5, hjust = 0.5),
          axis.title.y = element_text(color = "#1b365d", face = "bold", size = 10.5, hjust = 0.5),
          axis.text = element_text(color = "#5a6c7d", size = 9), axis.ticks = element_blank(),
          plot.background = element_rect(fill = "#fafafa", color = NA),
          panel.background = element_rect(fill = "#fafafa", color = NA),
          plot.margin = margin(6, 12, 6, 6))
  ggsave(outfile, p, width = w, height = h, dpi = 220, bg = "#fafafa", device = ragg::agg_png)
  cat("wrote", outfile, "\n")
}

A <- function(x,y,label,hjust,vjust,color) data.frame(x,y,label,hjust,vjust,color)

# ---- Slide 3: overall framework (evidence x readiness) ----
df3 <- data.frame(
  label = c("Large-scale food fortification","Breastfeeding promotion","Zinc (diarrhoea Rx)",
            "Vitamin A supplementation","Antenatal MMS","SQ-LNS",
            "CMAM / RUTF","Antenatal iron-folic acid","Periconception folic acid",
            "Complementary feeding","Micronutrient powders","Iron (children)",
            "Balanced energy-protein","WASH","Cash transfers"),
  x = c(9.0,7.7,8.6, 8.3,8.0,7.4, 8.1,7.3,7.8, 6.7,6.1,5.9, 5.7,4.0,2.9),
  y = c(9.1,8.5,7.9, 7.3,6.8,6.2, 4.9,4.5,4.0, 4.9,4.3,3.7, 3.3,3.6,2.9),
  tier = c(rep("T1",6), rep("T2",7), rep("T3",2)))
ann3 <- rbind(
  A(9.85,9.75,"Strong evidence + high readiness",1,1,"#46566a"), A(1.15,9.75,"Weak evidence + high readiness",0,1,"#46566a"),
  A(1.15,1.25,"Weak evidence + low readiness",0,0,"#46566a"), A(9.85,1.25,"Strong evidence + low readiness",1,0,"#46566a"))
quad_plot(df3, "Evidence Strength", "Implementation Readiness",
          c("Indirect (C)","Strong (A)"), c("Low","High"), ann3, "output/slide3_quadrant.png")

# ---- Slide 4: children under 5 (effect size x cost-effectiveness) ----
df4 <- data.frame(
  label = c("Vitamin A supplementation","Zinc (diarrhoea Rx)","SQ-LNS",
            "Complementary feeding","CMAM / RUTF","Micronutrient powders","Iron (children)"),
  x = c(8.0,7.3,8.4, 5.2,8.2,5.6,4.8),
  y = c(7.8,9.0,5.8, 6.2,4.0,5.4,5.0),
  tier = c("T1","T1","T1","T2","T2","T2","T2"))
ann4 <- rbind(A(9.85,9.75,"Large effect + high CE",1,1,"#46566a"), A(1.15,9.75,"Modest effect + high CE",0,1,"#46566a"),
              A(1.15,1.25,"Modest effect + low CE",0,0,"#46566a"), A(9.85,1.25,"Large effect + low CE",1,0,"#46566a"))
quad_plot(df4, "Effect Size", "Cost-Effectiveness",
          c("Moderate","Large"), c("Lower","Higher"), ann4, "output/slide4_children.png")

# ---- Slide 5: women of reproductive age (effect size x cost-effectiveness) ----
df5 <- data.frame(
  label = c("Antenatal MMS","Periconception folic acid","Antenatal iron-folic acid","Balanced energy-protein"),
  x = c(7.4,8.2,6.4,5.6),
  y = c(8.2,7.0,6.0,4.2),
  tier = c("T1","T2","T2","T2"))
ann5 <- rbind(A(9.85,9.75,"Large effect + high CE",1,1,"#46566a"), A(1.15,9.75,"Modest effect + high CE",0,1,"#46566a"),
              A(1.15,1.25,"Modest effect + low CE",0,0,"#46566a"), A(9.85,1.25,"Large effect + low CE",1,0,"#46566a"))
quad_plot(df5, "Effect Size", "Cost-Effectiveness",
          c("Moderate","Large"), c("Lower","Higher"), ann5, "output/slide5_wra.png")
