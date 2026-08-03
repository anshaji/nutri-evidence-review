# Full-corpus quadrant chart — all 23 interventions (evidence x readiness),
# reusing the slide_figures.R quad_plot style. Renders
# output/quadrant_23_interventions.png
suppressMessages({library(ggplot2); library(ggrepel); library(ragg)})
FONT <- "Helvetica Neue"
update_geom_defaults("text", list(family = FONT))

tx <- 5.5; ty <- 5.5
ARR <- "\u2192"; EMD <- "\u2014"   # arrow, em-dash
tier_cols   <- c(T1 = "#1e7a3c", T2 = "#2e5c8a", T3 = "#c0392b")
tier_labels <- c(T1 = paste("Tier 1", EMD, "strong + cost-effective"),
                 T2 = paste("Tier 2", EMD, "strong / mixed"),
                 T3 = paste("Tier 3", EMD, "promising / indirect"))

quad_plot <- function(df, xlab, ylab, xlabs, ylabs, annos, outfile, w = 9.6, h = 6.8) {
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
                      vjust = a$vjust, color = a$color, fontface = "bold", size = 3.0)
  }
  p <- p +
    geom_point(aes(color = tier), size = 3.6, alpha = 0.9) +
    geom_text_repel(aes(label = label), size = 3.05, color = "#1a1a2e", family = FONT,
                    box.padding = 0.55, point.padding = 0.3, min.segment.length = 0,
                    segment.color = "#9aa7b4", segment.size = 0.3, max.overlaps = Inf,
                    force = 3, force_pull = 0.6, seed = 7) +
    scale_color_manual(values = tier_cols[pres], labels = tier_labels[pres], name = NULL) +
    scale_x_continuous(limits = c(1, 10), breaks = c(2, 9), labels = xlabs, expand = c(0, 0)) +
    scale_y_continuous(limits = c(1, 10), breaks = c(2, 9), labels = ylabs, expand = c(0, 0)) +
    labs(x = paste(xlab, ARR), y = paste(ylab, ARR)) +
    theme_minimal(base_size = 12, base_family = FONT) +
    theme(legend.position = "top", legend.justification = "left",
          legend.text = element_text(size = 10, color = "#1a1a2e"), legend.margin = margin(0,0,2,0),
          panel.grid = element_blank(),
          axis.title.x = element_text(color = "#1b365d", face = "bold", size = 11, hjust = 0.5),
          axis.title.y = element_text(color = "#1b365d", face = "bold", size = 11, hjust = 0.5),
          axis.text = element_text(color = "#5a6c7d", size = 9.5), axis.ticks = element_blank(),
          plot.background = element_rect(fill = "#fafafa", color = NA),
          panel.background = element_rect(fill = "#fafafa", color = NA),
          plot.margin = margin(6, 12, 6, 6))
  ggsave(outfile, p, width = w, height = h, dpi = 220, bg = "#fafafa", device = ragg::agg_png)
  cat("wrote", outfile, "\n")
}
A <- function(x,y,label,hjust,vjust,color) data.frame(x,y,label,hjust,vjust,color)

# x = Evidence Strength (C left ~ A right; B-with-real-MAs right of divider,
#     observational-only B/C left). y = Implementation Readiness (scalability:
#     Proven national high -> Requires investment low).
df <- data.frame(
  label = c(
    # Tier 1
    "Large-scale food fortification","Breastfeeding promotion","Vitamin A supplementation",
    "Zinc (diarrhoea Rx)","Complementary feeding","Antenatal MMS",
    "CMAM / RUTF","Periconception folic acid",
    # Tier 2
    "Cash transfers","Antenatal iron-folic acid","Social protection",
    "SQ-LNS","Child multiple micronutrients","Balanced energy-protein",
    "Maternal nutrition (ANC)","Iron (children)","Micronutrient powders","Multisectoral packages",
    # Tier 3
    "School feeding","WASH","Nutrition-sensitive agriculture","Growth monitoring","Vitamin D (children)"),
  x = c(
    8.7, 7.9, 8.2, 8.6, 7.4, 8.4, 6.6, 6.9,
    7.7, 6.6, 4.9, 7.9, 7.2, 7.6, 6.0, 6.2, 5.8, 5.2,
    3.0, 5.4, 5.0, 3.4, 3.2),
  y = c(
    9.0, 8.6, 8.0, 5.4, 6.4, 3.9, 8.3, 7.6,
    7.9, 7.2, 7.8, 4.0, 5.0, 3.4, 3.6, 3.1, 5.0, 5.2,
    7.6, 3.0, 3.4, 5.0, 3.4),
  tier = c(rep("T1",8), rep("T2",10), rep("T3",5)))

ann <- rbind(
  A(9.85,9.75,"Strong evidence + high readiness",1,1,"#46566a"),
  A(1.15,9.75,"Weak evidence + high readiness",0,1,"#46566a"),
  A(1.15,1.25,"Weak evidence + low readiness",0,0,"#46566a"),
  A(9.85,1.25,"Strong evidence + low readiness",1,0,"#46566a"))

quad_plot(df, "Evidence Strength", "Implementation Readiness",
          c("Indirect (C)","Strong (A)"), c("Low","High"), ann,
          "output/quadrant_23_interventions.png")
