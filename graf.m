A="C:\Users\ynish\Desktop\gitpractice\clone\tmp\df1.csv";%%%�p�X��ǉ����ĉ�����
c=readmatrix(A);
plot(c(1:size(c,1),2),[c(1:size(c,1),3) c(1:size(c,1),4) c(1:size(c,1),5)]);
title('3���Ԃɂ����鉷�x����');
xlabel('�o�ߎ���(��)');
ylabel('���x(��)');
legend('���ω��x','�ō����x','�Œቷ�x');
saveas(gcf,'tmp.png');
