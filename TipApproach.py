import tkinter as tk

class TipApproach(tk.Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("Tip Approach")
        
        # 프레임 생성
        frame = tk.Frame(self.master, bd=2, relief=tk.GROOVE)
        frame.pack(side=tk.LEFT, padx=10, pady=10)
        

                
        frame_waveform_control = tk.LabelFrame(frame, text="Waveform Control", width=185, height=129)
        frame_waveform_control.place(x=11, y=8)

        frame_delay = tk.LabelFrame(frame_waveform_control, text="Delay", width=80, height=50)
        frame_delay.place(x=19, y=21)

        frame_xo_step_size = tk.LabelFrame(frame_waveform_control, text="xo Step Size", width=80, height=55)
        frame_xo_step_size.place(x=19, y=75)

        frame_zo_step_size = tk.LabelFrame(frame_waveform_control, text="zo Step Size", width=80, height=55)
        frame_zo_step_size.place(x=107, y=75)

        frame_steps = tk.LabelFrame(frame, text="Steps", width=100, height=45)
        frame_steps.place(x=10, y=142)

        frame_acceleration = tk.LabelFrame(frame, text="Acceleration", width=80, height=50)
        frame_acceleration.place(x=107, y=21)

        frame_min_tunneling_current = tk.LabelFrame(frame, text="Min Tunneling Current", width=88, height=51)
        frame_min_tunneling_current.place(x=207, y=44)

        frame_approach_parameters = tk.LabelFrame(frame, text="Approach Parameters", width=146, height=42)
        frame_approach_parameters.place(x=207, y=95)

        frame_sample_type = tk.LabelFrame(frame, text="Sample Type", width=157, height=32)
        frame_sample_type.place(x=257, y=4)

        frame_dosed_with = tk.LabelFrame(frame, text="Dosed With", width=116, height=32)
        frame_dosed_with.place(x=298, y=37)

        # 코드에 간결함을 위해 일부 위젯만 작성하였습니다.
        # 비슷한 방법으로 나머지 위젯도 작성할 수 있습니다.
        entry_tip_delay_edit = tk.Entry(frame_delay, width=5)
        entry_tip_delay_edit.place(x=53, y=39)

        entry_tip_x_step_bits_edit = tk.Entry(frame_xo_step_size, width=5)
        entry_tip_x_step_bits_edit.place(x=63, y=99)

        entry_tip_x_step_volts_edit = tk.Entry(frame_xo_step_size, width=5)
        entry_tip_x_step_volts_edit.place(x=27, y=99)

        entry_tip_zo_step_bits_edit = tk.Entry(frame_zo_step_size, width=5)
        entry_tip_zo_step_bits_edit.place(x=152, y=99)

        entry_tip_zo_step_volts_edit = tk.Entry(frame_zo_step_size, width=5)
        entry_tip_zo_step_volts_edit.place(x=115, y=99)

        entry_tip_number_edit = tk.Entry(frame_steps, width=5)
        entry_tip_number_edit.place(x=72, y=152)

        entry_tip_accel_edit = tk.Entry(frame_acceleration, width=5)
        entry_tip_accel_edit.place(x=148, y=37)

        entry_tip_tunnel_bits = tk.Entry(frame_min_tunneling_current, width=5)
        entry_tip_tunnel_bits.place(x=256, y=64)

        entry_tip_tunnel_volts = tk.Entry(frame_min_tunneling_current, width=5)
        entry_tip_tunnel_volts.place


        # # Acceleration 그룹박스
        # acc_groupbox = tk.LabelFrame(frame, text="Acceleration", padx=5, pady=5)
        # acc_groupbox.grid(row=0, column=0, padx=5, pady=5)
        
        # acc_edit = tk.Entry(acc_groupbox, width=5)
        # acc_edit.grid(row=0, column=0, padx=5, pady=5)
        # acc_edit.insert(0, "0")
        
        # acc_scroll = tk.Scale(acc_groupbox, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        # acc_scroll.set(0)
        # acc_scroll.grid(row=1, column=0, padx=5, pady=5)
        
        # # Delay 그룹박스
        # delay_groupbox = tk.LabelFrame(frame, text="Delay", padx=5, pady=5)
        # delay_groupbox.grid(row=1, column=0, padx=5, pady=5)
        
        # delay_edit = tk.Entry(delay_groupbox, width=5)
        # delay_edit.grid(row=0, column=0, padx=5, pady=5)
        # delay_edit.insert(0, "0")
        
        # delay_scroll = tk.Scale(delay_groupbox, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        # delay_scroll.set(0)
        # delay_scroll.grid(row=1, column=0, padx=5, pady=5)
        
        # delay_unit = tk.Label(delay_groupbox, text="ms")
        # delay_unit.grid(row=0, column=1, padx=5, pady=5)
        
        # # xo Step Size 그룹박스
        # xo_groupbox = tk.LabelFrame(frame, text="xo Step Size", padx=5, pady=5)
        # xo_groupbox.grid(row=2, column=0, padx=5, pady=5)
        
        # xo_bits_edit = tk.Entry(xo_groupbox, width=5)
        # xo_bits_edit.grid(row=0, column=0, padx=5, pady=5)
        # xo_bits_edit.insert(0, "0")
        
        # xo_scroll = tk.Scale(xo_groupbox, from_=0, to=100, orient=tk.HORIZONTAL, length=100)
        # xo_scroll.set(0)
        # xo_scroll.grid(row=1, column=0, padx=5, pady=5)
        
        # xo_unit = tk.Label(xo_groupbox, text="Bits")
        # xo_unit.grid(row=0, column=1, padx=5, pady=5)
        
        # xo_volts_edit = tk.Entry(xo_groupbox, width=5)
        # xo_volts_edit.grid(row=2, column=0, padx=5, pady=5)
        # xo_volts_edit.insert(0, "0")
        
        # xo_volts_unit = tk.Label(xo_groupbox, text="Volts")
        # xo_volts_unit.grid(row=2, column=1, padx=5, pady=5)
        
        # xo_scroll2 = tk.Scale(xo_groupbox, from_=0, to=100) # 마무리 안됨.

        # xo_groupbox = tk.LabelFrame(frame, text="xo Step Size", padx=5, pady=5)
        # xo_groupbox.place(x=19, y=75)

        # # xo_step_volts_edit and xo_step_scroll
        # xo_step_volts_label = tk.Label(xo_groupbox, text="Volts")
        # xo_step_volts_label.grid(row=0, column=2, padx=5, pady=5)

        # xo_step_volts_edit = tk.Entry(xo_groupbox, width=7)
        # xo_step_volts_edit.grid(row=0, column=1, padx=5, pady=5)

        # xo_step_scroll = tk.Scrollbar(xo_groupbox, orient=tk.HORIZONTAL)
        # xo_step_scroll.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="EW")

        # # xo_step_bits_edit
        # xo_step_bits_label = tk.Label(xo_groupbox, text="Bits")
        # xo_step_bits_label.grid(row=0, column=4, padx=5, pady=5)

        # xo_step_bits_edit = tk.Entry(xo_groupbox, width=5)
        # xo_step_bits_edit.grid(row=0, column=3, padx=5, pady=5)

        # # xo_step_volts_edit와 xo_step_scroll 연결
        # xo_step_volts_edit.config(xscrollcommand=xo_step_scroll.set)
        # xo_step_scroll.config(command=xo_step_volts_edit.xview)

        # zo_groupbox = tk.LabelFrame(frame, text="zo Step Size", padx=5, pady=5)
        # zo_groupbox.place(x=107, y=75)

        # # zo_step_volts_edit and zo_step_scroll
        # zo_step_volts_label = tk.Label(zo_groupbox, text="Volts")
        # zo_step_volts_label.grid(row=0, column=2, padx=5, pady=5)

        # zo_step_volts_edit = tk.Entry(zo_groupbox, width=7)
        # zo_step_volts_edit.grid(row=0, column=1, padx=5, pady=5)

        # zo_step_scroll = tk.Scrollbar(zo_groupbox, orient=tk.HORIZONTAL)
        # zo_step_scroll.grid(row=1, column=0, columnspan=3, padx=5, pady=5, sticky="EW")

        # # zo_step_bits_edit
        # zo_step_bits_label = tk.Label(zo_groupbox, text="Bits")
        # zo_step_bits_label.grid(row=0, column=4, padx=5, pady=5)

        # zo_step_bits_edit = tk.Entry(zo_groupbox, width=5)
        # zo_step_bits_edit.grid(row=0, column=3, padx=5, pady=5)

        # # zo_step_volts_edit와 zo_step_scroll 연결
        # zo_step_volts_edit.config(xscrollcommand=zo_step_scroll.set)
        # zo_step_scroll.config(command=zo_step_volts_edit.xview)

        # # tip_zo_edit
        # tip_zo_label = tk.Label(frame, text="Tunneled At:")
        # tip_zo_label.place(x=135, y=216)

        # tip_zo_edit = tk.Entry(frame, width=7, state="readonly")
        # tip_zo_edit.place(x=188, y=214)

        # # tip_status
        # tip_status_label = tk.Label(frame, text="Status:")
        # tip_status_label.place(x=134, y=202)

        # tip_status = tk.Label(frame, text="", width=12, anchor="w", relief="sunken")
        # tip_status.place(x=168, y=202)

        # # tip_pass_num
        # tip_pass_num_label = tk.Label(frame, text="Pass #")
        # tip_pass_num_label.place(x=257, y=202) # 마무리 안됨
        
    def new_button_clicked(self):
        print("New button clicked!")