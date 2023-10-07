using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
using Python.Runtime;

namespace Oasis
{
    /// <summary>
    /// Interaction logic for Window1.xaml
    /// </summary>
   public partial class ChatWindow : Window
   {
    public ChatWindow()
    {
        if (!PythonEngine.IsInitialized)
        {
            Runtime.PythonDLL = @"C:\Users\Lenovo\AppData\Local\Programs\Python\Python39\python39.dll";
            PythonEngine.Initialize();
        }
        InitializeComponent();
        double height = SystemParameters.PrimaryScreenHeight;
        double width = SystemParameters.PrimaryScreenWidth;
        double chat_height = (65 * height) / 100;
        double chat_width = (25 * width) / 100;
        this.WindowStartupLocation = WindowStartupLocation.Manual;
        this.ResizeMode=ResizeMode.NoResize;
        this.Height = chat_height;
        this.Width = chat_width;
        this.Left = (width - chat_width)+((1.5*Width)/100);
        this.Top = ((height - chat_height)-((4.7* height)/100));

    }
   }
}
