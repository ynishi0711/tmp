A="C:\Users\ynish\Desktop\gitpractice\clone\tmp\df1.csv";%%%パスを追加して下さい
c=readmatrix(A);
plot(c(1:size(c,1),2),[c(1:size(c,1),3) c(1:size(c,1),4) c(1:size(c,1),5)]);
title('3時間における温度推移');
xlabel('経過時間(分)');
ylabel('温度(℃)');
legend('平均温度','最高温度','最低温度');
saveas(gcf,'tmp.png');
