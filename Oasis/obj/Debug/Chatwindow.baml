   M S B A M L   `   `   `  ����@  <Oasis, Version=1.0.0.0, Culture=neutral, PublicKeyToken=nullclr-namespace:OasisOasis  5   	       Oasis.ChatWindow   5   	   R NWindowsBase, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35W SPresentationCore, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35\ XPresentationFramework, Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35D 9http://schemas.microsoft.com/winfx/2006/xaml/presentation    5   	   R NSystem.Xaml, Version=4.0.0.0, Culture=neutral, PublicKeyToken=b77a5c561934e089:x,http://schemas.microsoft.com/winfx/2006/xaml     5   	   @d2http://schemas.microsoft.com/expression/blend/2008     5   	   Jmc;http://schemas.openxmlformats.org/markup-compatibility/2006     5   	   %localclr-namespace:Oasis     5   	     � Title$  Oasis��5   	   .��5	      � .+�5
   
   � $��0,0,0,0q�6   .+�5      ]� ��. .+�5      �� $��Bottom=�6   $��0 0 0 0 q�61   ���	#35B3B3B3���	#59FF0000$��2q�6r    �� CornerRadius$ 20,20,20,20��6�   ._�5      � .+�5      �� -   5         ��Name$ bottom_query��5   "   $��10q�68   ���	#003E3E3E
���   ����	#FF4A4A4A$��Baskerville old face)�5      $��20(�6<   $��0q�6J   $��0 0 65 0q�6^   .��6�   5      5      5      �� 5      -   5         ��Name$ ChatScrollViewer��5      $��Hidden=�69   .��5      �� -   5         ��Name$ ItemsControl��5   D   ��6#   �� *
Messages+��5      �� 5      .R�5   "   � $
��auto��6'   $��
15 2 20 10q�65    � ColumnDefinitions 5   &   �� 5   *   $��* �6;   �� 5   *   $
��Auto �6;   .+�5    &   �� $ 8��6-   
�������$��0q�6w    �� Padding$ 10q�5!   %   $
��Left=�62   ��5    @   �� *Column+��5"   *   �� 5#   .    �� 
TargetType" ��64   .�5$   2   ��  �� Property � ��	 �� Value	 �#F0F0F06O   
 �� Triggers
 5%   2   �� 5&   6    �� Binding 6B   �� *Column+ �� Value 16]   .a�5'   :   ��  � ��
	 ��ح�6W   5(   7   5*   /    J� Effect 5,   *   3  -System.Windows.Media.Effects.DropShadowEffect  5.   .      
BlurRadius$ 5Q�6?      Color$ Black��6N      Opacity$ .3Q�6\      ShadowDepth$ 1Q�6j   ._�51   *   ��  �� Orientation$ Vertical=�65   .+�52   .   �� $	��300��6k    �� TextWrapping$
 Wrap=�6z   
���   �$��times new roman)�6�   $��18(�53       �� 
IsReadOnly . 
������ $��0q�6G   ��52   6   �� *Text+��6L   �� *Column+.��53   [   ��54   2   �� 55   6   " ��6<   .�56   :   ��  � ��	 �#F0F0F06W   
 57   :   �� 58   >    6J   �� *Column+ 16e   .a�59   B   ��  � ��
	 ��ح�6_   5:   ?   5<   7   .��5=   A   5>   /   �� 5A   2    ��Name$ imagined_image��68   $	��150��6Q   ��5B   6   �� 5C   :   " ��6@   .�5D   >   ��  � y�$	 	Collapsed=�6[   
 5E   >   �� 5F   B    6N   �� *Column+ 06i   .a�5G   F   ��  � y�$	 Visible=�6c   5H   C   5J   ;   5L   3   5R   +   5U   '   5Y   #   5\      5^      5`      5b      5e      5f      5g      